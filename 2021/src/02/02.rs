use std::{
    fs::File,
    io::{prelude::*, BufReader},
    path::Path,
};

fn get_data(filename: impl AsRef<Path>) -> Vec<(String, i32)> {
    let file = File::open(filename).expect("File not found");
    let buf = BufReader::new(file);
    let lines = buf.lines()
        .map(|l| l.expect("Could not parse line"))
        .collect::<Vec<String>>();
    let mut pairs = Vec::new();
    for line in lines {
        let split: Vec<String> = line.split_whitespace().map(String::from).collect();
        pairs.push((split[0].clone(), split[1].parse().unwrap()))
    }
    pairs
}

fn part_one() {
    let mut horizontal_pos = 0;
    let mut depth = 0;
    for line in get_data("../../data/02.txt") {
        if line.0 == "forward" {
            horizontal_pos += line.1
        }
        else if line.0 == "down" { 
            depth += line.1
        }
        else if line.0 == "up" {
            depth -= line.1
        }
    }

    println!("Horizontal Position: {}", horizontal_pos);
    println!("Depth: {}", depth);
    println!("Product: {}", horizontal_pos * depth)
}

fn part_two() {
}

fn main() {
    println!("Part One");
    part_one();
    println!("Part Two");
    part_two();
}