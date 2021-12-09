use std::{
    fs::File,
    io::{prelude::*, BufReader},
    path::Path,
};

fn get_bingo_calls(filename: impl AsRef<Path>) -> Vec<u32> {
    let file = File::open(filename).expect("File not found");
    let mut buf = BufReader::new(file);
    let mut bingo_calls = String::new();
    buf.read_line(&mut bingo_calls)
        .expect("Unable to read line from file");
    bingo_calls
        .split(',')
        .map(|num| num.trim().parse::<u32>().expect("Error parsing number"))
        .collect()
}

fn get_boards(filename: impl AsRef<Path>) -> Vec<Vec<Vec<u32>>> {
    let file = File::open(filename).expect("File not found");
    let buf = BufReader::new(file);
    let lines = buf
        .lines()
        .skip(2)
        .map(|l| l.expect("Could not parse line"))
        .collect::<Vec<String>>();

    let mut boards = Vec::new();

    // Loop over boards
    let mut i = 0;
    loop {
        let mut board = Vec::new();
        if i >= lines.len() {
            break;
        }
        let mut j = 0;
        // Loop over board rows
        loop {
            if i + j >= lines.len() || lines[i + j].len() == 0 {
                j += 1;
                break;
            }

            board.push(
                lines[i + j]
                    .split_whitespace()
                    .map(|num| {
                        num.trim()
                            .parse::<u32>()
                            .expect(&format!("Error parsing number {}", num))
                    })
                    .collect(),
            );

            j += 1;
        }
        boards.push(board);
        i += j;
    }

    return boards;
}

fn part_one() {
    let filename = "input.txt";
    let bingo_calls = get_bingo_calls(format!("data/{}", filename));
    let boards = get_boards(format!("data/{}", filename));

    let (winning_board_num, called_numbers) = run_bingo(&boards, &bingo_calls);
    let winning_board_num: usize = winning_board_num.expect("No winner!");

    println!(
        "Board {} wins after {} calls",
        winning_board_num + 1,
        called_numbers.len()
    );
    println!("Called numbers: {:?}", called_numbers);

    let mut unmarked_sum = 0;
    for row in &boards[winning_board_num] {
        for num in row {
            if !called_numbers.contains(num) {
                unmarked_sum += num;
            }
        }
    }

    println!("Unmarked sum: {}", unmarked_sum);

    println!(
        "Final score: {}",
        unmarked_sum * called_numbers[called_numbers.len() - 1]
    );
}

fn part_two() {
    let filename = "input.txt";
    let bingo_calls = get_bingo_calls(format!("data/{}", filename));
    let mut boards = get_boards(format!("data/{}", filename));

    let mut winning_board_num;
    let mut called_numbers;
    loop {
        let (_winning_board_num, _called_numbers) = run_bingo(&boards, &bingo_calls);
        winning_board_num = _winning_board_num.expect("No winner!");
        called_numbers = _called_numbers;

        if boards.len() == 1 {
            break;
        }

        boards.remove(winning_board_num);
    }

    println!(
        "Board {} wins after {} calls",
        winning_board_num + 1,
        called_numbers.len()
    );
    println!("Called numbers: {:?}", called_numbers);

    let mut unmarked_sum = 0;
    for row in &boards[winning_board_num] {
        for num in row {
            if !called_numbers.contains(num) {
                unmarked_sum += num;
            }
        }
    }

    println!("Unmarked sum: {}", unmarked_sum);

    println!(
        "Final score: {}",
        unmarked_sum * called_numbers[called_numbers.len() - 1]
    );
}

fn run_bingo(boards: &Vec<Vec<Vec<u32>>>, bingo_calls: &Vec<u32>) -> (Option<usize>, Vec<u32>) {
    let mut results = Vec::new();
    for board in boards {
        let mut blank_board = Vec::<Vec<bool>>::new();
        for row in board {
            let blank_row = vec![false; row.len()];
            blank_board.push(blank_row);
        }
        results.push(blank_board);
    }

    let mut called_numbers = Vec::new();
    let mut winning_board_num = None;
    for bingo_call in bingo_calls {
        called_numbers.push(*bingo_call);
        for (i, board) in boards.iter().enumerate() {
            for (j, row) in board.iter().enumerate() {
                for (k, num) in row.iter().enumerate() {
                    if num == bingo_call {
                        results[i][j][k] = true;
                    }
                }
            }
        }

        let mut winner = false;
        for (board_num, result_board) in results.iter().enumerate() {
            let mut board_wins = false;
            for row in result_board {
                let mut row_wins = true;
                for num in row {
                    if !*num {
                        row_wins = false;
                        break;
                    }
                }
                if row_wins {
                    board_wins = true;
                    break;
                }
            }

            for col_num in 0..result_board[0].len() {
                let mut col_wins = true;
                for row_num in 0..result_board.len() {
                    if !result_board[row_num][col_num] {
                        col_wins = false;
                        break;
                    }
                }
                if col_wins {
                    board_wins = true;
                    break;
                }
            }

            if board_wins {
                winner = true;
                winning_board_num = Some(board_num);
                break;
            }
        }

        if winner {
            break;
        }
    }

    return (winning_board_num, called_numbers);
}

fn main() {
    println!("Part One");
    part_one();
    println!("Part Two");
    part_two();
}
