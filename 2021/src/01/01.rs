use std::{
    fs::File,
    io::{prelude::*, BufReader},
    path::Path,
};

fn get_data(filename: impl AsRef<Path>) -> Vec<i32> {
    let file = File::open(filename).expect("File not found");
    let buf = BufReader::new(file);
    buf.lines()
        .map(|l| l.expect("Could not parse line"))
        .map(|l| l.parse().unwrap())
        .collect()
}

fn main() {
    let data = get_data("../../data/01.txt");
    let mut count = 0;
    for i in 0..data.len() {
        if i == 0 {
            continue;
        }
        if data[i] > data[i-1] {
            count += 1;
        }
    }

    println!("{}", count)
}