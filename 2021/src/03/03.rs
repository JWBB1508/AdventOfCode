use std::{
    fs::File,
    io::{prelude::*, BufReader},
    path::Path,
};

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
    for i in 0..length {
        let mut count_1 = 0;
        for value in &values {
            if value.chars().nth(i) == Some('1') {
                count_1 += 1;
            }
        }

        if count_1 > values.len() / 2 {
            gamma_rate_bits.push('1');
            epsilon_rate_bits.push('0');
        } else {
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
    let values = get_data_str("../../data/03.txt");
    let length = values[0].len();
    let mut oxygen_rating_bits = values.to_vec();
    let mut co2_rating_bits = values.to_vec();
    for i in 0..length {
        if &oxygen_rating_bits.len() > &1 {
            oxygen_rating_bits = most_common_filter(oxygen_rating_bits, i);
        }

        if &co2_rating_bits.len() > &1 {
            co2_rating_bits = least_common_filter(co2_rating_bits, i);
        }
    }

    if oxygen_rating_bits.len() != 1 || co2_rating_bits.len() != 1 {
        panic!("Filtering failed");
    }

    let oxy_rating = i32::from_str_radix(&oxygen_rating_bits[0], 2).unwrap();
    let co2_rating = i32::from_str_radix(&co2_rating_bits[0], 2).unwrap();

    println!("Oxygen Generation Rating: {}", oxy_rating);
    println!("CO2 Scrubber Rating: {}", co2_rating);

    println!("Life Support Rating: {}", oxy_rating * co2_rating);
}

fn most_common_filter(mut bits_vec: Vec<String>, index: usize) -> Vec<String> {
    let mut count_1 = 0;
    for bits in &bits_vec {
        if bits.chars().nth(index) == Some('1') {
            count_1 += 1
        }
    }

    let most_common;
    if count_1 >= bits_vec.len() - count_1 {
        most_common = '1';
    } else {
        most_common = '0';
    }

    bits_vec.retain(|bits| bits.chars().nth(index) == Some(most_common));
    return bits_vec;
}

fn least_common_filter(mut bits_vec: Vec<String>, index: usize) -> Vec<String> {
    let mut count_1 = 0;
    for bits in &bits_vec {
        if bits.chars().nth(index) == Some('1') {
            count_1 += 1
        }
    }

    let most_common;
    if count_1 >= bits_vec.len() - count_1 {
        most_common = '1';
    } else {
        most_common = '0';
    }

    bits_vec.retain(|bits| bits.chars().nth(index) != Some(most_common));
    return bits_vec;
}

fn main() {
    println!("Part One");
    part_one();
    println!("Part Two");
    part_two();
}
