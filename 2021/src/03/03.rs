use std::{
    fs::File,
    io::{prelude::*, BufReader},
    path::Path,
};

fn get_data_int(filename: impl AsRef<Path>) -> Vec<i32> {
    let file = File::open(filename).expect("File not found");
    let buf = BufReader::new(file);
    buf.lines()
        .map(|l| l.expect("Could not parse line"))
        .map(|l| i32::from_str_radix(&l, 2).unwrap())
        .collect()
}

fn get_data_str(filename: impl AsRef<Path>) -> Vec<String> {
    let file = File::open(filename).expect("File not found");
    let buf = BufReader::new(file);
    buf.lines()
        .map(|l| l.expect("Could not parse line"))
        .collect()
}

fn part_one() {
    let values = get_data_str("../../data/03.txt");
    let length = values[0].len();
    let mut gamma_rate_bits = String::from("");
    let mut epsilon_rate_bits = String::from("");
    for i in 0..length{
        let mut count_1 = 0;
        for value in &values {
            if value.chars().nth(i) == Some('1') {
                count_1 += 1;
            }
        }

        if count_1 > values.len() / 2 {
            gamma_rate_bits.push('1');
            epsilon_rate_bits.push('0');
        }
        else {
            gamma_rate_bits.push('0');
            epsilon_rate_bits.push('1');
        }
    }

    let gamma_rate = i32::from_str_radix(&gamma_rate_bits, 2).unwrap();
    let epsilon_rate = i32::from_str_radix(&epsilon_rate_bits, 2).unwrap();

    println!("Gamma Rate: {}", gamma_rate);
    println!("Epsilon Rate: {}", epsilon_rate);

    println!("Power Cosumption: {}", gamma_rate * epsilon_rate)
}

fn part_two() {
}

fn main() {
    println!("Part One");
    part_one();
    println!("Part Two");
    part_two();
}