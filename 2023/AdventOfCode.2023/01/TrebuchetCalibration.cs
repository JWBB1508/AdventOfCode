using AdventOfCode._2023.Library;
using System.Text.RegularExpressions;

namespace AdventOfCode._2023._01
{
    internal class TrebuchetCalibration : APuzzle
    {
        private readonly Regex _digitRegex;

        public TrebuchetCalibration(string dataFilename, Part part)
            : base(dataFilename, part)
        {
            _digitRegex = part switch
            {
                Part.One => new(@"\d"),
                Part.Two => new(@"one|two|three|four|five|six|seven|eight|nine|\d"),
                _ => throw new ArgumentOutOfRangeException(nameof(part), part, "Invalid Part"),
            };
        }

        public override string GetAnswer()
        {
            return GetCalibrationValue().ToString();
        }

        private decimal GetCalibrationValue()
        {
            return File.ReadLines(DataFilename)
                .Select(x => GetDigits(x))
                .Select(x => decimal.Parse($"{x.First}{x.Last}"))
                .Sum();
        }

        private (short First, short Last) GetDigits(string line)
        {
            IList<Match> matches = new List<Match>();
            Match match = _digitRegex.Match(line);
            while (match.Success)
            {
                // Need to do this instead of simply _digitRegex.Matches() to catch overlapping matches
                // e.g. "twone"
                matches.Add(match);
                match = _digitRegex.Match(line, match.Index + 1);
            }

            return (ConvertDigit(matches.First().Value), ConvertDigit(matches.Last().Value));
        }

        private static short ConvertDigit(string digit)
        {
            return digit switch
            {
                "one" => 1,
                "two" => 2,
                "three" => 3,
                "four" => 4,
                "five" => 5,
                "six" => 6,
                "seven" => 7,
                "eight" => 8,
                "nine" => 9,
                _ => short.Parse(digit),
            };
        }
    }
}
