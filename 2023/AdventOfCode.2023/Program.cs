using AdventOfCode._2023._01;
using AdventOfCode._2023.Library;

const string Day = "01";

Console.WriteLine(Part.One);

Console.WriteLine(new TrebuchetCalibration($"{Day}/example-one.txt", Part.One).GetCalibrationValue());
Console.WriteLine(new TrebuchetCalibration($"{Day}/data.txt", Part.One).GetCalibrationValue());

Console.WriteLine(Part.Two);

Console.WriteLine(new TrebuchetCalibration($"{Day}/example-two.txt", Part.Two).GetCalibrationValue());
Console.WriteLine(new TrebuchetCalibration($"{Day}/data.txt", Part.Two).GetCalibrationValue());