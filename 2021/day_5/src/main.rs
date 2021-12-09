use std::{
    cmp,
    fs::File,
    io::{prelude::*, BufReader},
    path::Path,
};

use itertools::Itertools;

fn get_lines(filename: impl AsRef<Path>) -> Vec<((usize, usize), (usize, usize))> {
    let file = File::open(filename).expect("File not found");
    let buf = BufReader::new(file);
    let file_lines = buf
        .lines()
        .map(|l| l.expect("Could not parse line"))
        .collect::<Vec<String>>();

    let mut lines = Vec::new();
    for file_line in file_lines {
        let coord_pairs: Vec<usize> = file_line
            .split("->")
            .map(|pair| {
                pair.split(",")
                    .map(|coord| {
                        coord
                            .trim()
                            .parse::<usize>()
                            .expect(&format!("Error parsing coord: {}", coord))
                    })
                    .collect::<Vec<usize>>()
            })
            .flatten()
            .collect();
        for (x1, y1, x2, y2) in coord_pairs.into_iter().tuples() {
            lines.push(((x1, y1), (x2, y2)));
        }
    }

    return lines;
}

fn part_one() {
    let lines = get_lines("data/test_input.txt");

    let x_min = lines
        .iter()
        .map(|line| line.0 .0)
        .chain(lines.iter().map(|line| line.1 .0))
        .min()
        .expect("Error finding minimum x value");
    let x_max = lines
        .iter()
        .map(|line| line.0 .0)
        .chain(lines.iter().map(|line| line.1 .0))
        .max()
        .expect("Error finding maximum x value");
    let y_min = lines
        .iter()
        .map(|line| line.0 .1)
        .chain(lines.iter().map(|line| line.1 .1))
        .min()
        .expect("Error finding minimum y value");
    let y_max = lines
        .iter()
        .map(|line| line.0 .1)
        .chain(lines.iter().map(|line| line.1 .1))
        .max()
        .expect("Error finding maximum y value");

    let mut map = vec![vec![0; y_max - y_min]; x_max - x_min];
    for line in &lines {
        let ((x1, y1), (x2, y2)) = line;
        if x1 != x2 && y1 != y2 {
            // Line is not horizontal or vertical
            continue;
        }

        // TODO: for every point on the line, increment the corresponding value in map
    }
}

fn part_two() {}

fn main() {
    println!("Part One");
    part_one();
    println!("Part Two");
    part_two();
}
