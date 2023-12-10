using AdventOfCode._2023.Library;
using System.Text.RegularExpressions;

namespace AdventOfCode._2023._04
{
    internal class ScratchcardResolver : APuzzle
    {
        public ScratchcardResolver(string dataFilename, Part part) : base(dataFilename, part)
        { }

        public override string GetAnswer()
        {
            IEnumerable<Scratchcard> scratchcards = File.ReadAllLines(DataFilename).Select(Scratchcard.FromData);

            switch (Part)
            {
                case Part.One:
                    return scratchcards.Sum(x => x.Value).ToString();
                case Part.Two:
                    IDictionary<int, int> cardCount = scratchcards.ToDictionary(x => x.CardNumber, x => 1);
                    foreach (var scratchcard in scratchcards)
                    {
                        for (int i = scratchcard.CardNumber + 1;
                            i <= scratchcard.CardNumber + scratchcard.WinningNumberCount;
                            i++)
                        {
                            cardCount[i] += cardCount[scratchcard.CardNumber];
                        }
                    }
                    return cardCount.Values.Sum().ToString();
                default:
                    throw new InvalidOperationException($"Unknown Part: {Part}");
            }
        }

        private class Scratchcard
        {
            private readonly IEnumerable<int> _winningNumbers;
            private readonly IEnumerable<int> _numbers;

            private Scratchcard(int cardNumber, IEnumerable<int> winningNumbers, IEnumerable<int> numbers)
            {
                CardNumber = cardNumber;

                _winningNumbers = winningNumbers;
                _numbers = numbers;
            }

            public int CardNumber { get; }

            public int Value => (int)Math.Pow(2, _numbers.Intersect(_winningNumbers).Count() - 1);

            public int WinningNumberCount => _numbers.Intersect(_winningNumbers).Count();

            public static Scratchcard FromData(string line)
            {
                var matches = Regex.Match(line, @"Card\s+(\d+):\s+([\d\s]*)\|\s+([\d\s]*)$");

                return new Scratchcard(
                    int.Parse(matches.Groups[1].Value),
                    matches.Groups[2].Value.Split(
                        (char[]?)null,
                        StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries)
                    .Select(int.Parse),
                    matches.Groups[3].Value.Split(
                        (char[]?)null,
                        StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries)
                    .Select(int.Parse));
            }

        }
    }
}