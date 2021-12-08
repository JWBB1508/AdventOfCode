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
        .skip(1)
        .map(|l| l.expect("Could not parse line"));

    let mut boards = Vec::new();
    for line in lines {
        // TODO: Create boards, on blank line, jump to next board
        boards.push(
            line.map(|l| match l.len() {
                0 => Vec::new(),
                _ => l
                    .split_whitespace()
                    .map(|num| {
                        String::from(num)
                            .trim()
                            .parse::<u32>()
                            .expect(&format!("Error parsing number {}", num))
                    })
                    .collect(),
            })
            .collect(),
        );
    }

    return boards;
}

fn part_one() {
    let filename = "test_input.txt";

    let bingo_calls = get_bingo_calls(format!("data/{}", filename));
    println!("{:?}", bingo_calls);

    let boards = get_boards(format!("data/{}", filename));
    for board in boards {
        println!("{:?}", board);
    }
}

fn main() {
    part_one();
}
