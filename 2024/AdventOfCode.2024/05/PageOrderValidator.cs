using AdventOfCode._2024.Library;
using System.Text.RegularExpressions;

namespace AdventOfCode._2024._05
{
    internal class PageOrderValidator : APuzzle
    {
        private readonly Regex _ruleRegex;
        private readonly Regex _updateRegex;

        public PageOrderValidator(string dataFilename, Part part) : base(dataFilename, part)
        {
            _ruleRegex = new Regex(@"\d+\|\d+");
            _updateRegex = new Regex(@"(\d+,)*\d+");
        }

        public override string GetAnswer()
        {
            GetRulesAndUpdates(out List<PageOrderingRule> rules, out List<int[]> pageUpdates);

            switch (Part)
            {
                case Part.One:
                    return GetCorrectUpdateSum(rules, pageUpdates);
                case Part.Two:
                    return GetCorrectedIncorrectUpdateSum(rules, pageUpdates);
                default:
                    throw new NotSupportedException();
            }
        }

        private static string GetCorrectUpdateSum(List<PageOrderingRule> rules, List<int[]> pageUpdates)
        {
            int sum = 0;
            foreach (var update in pageUpdates)
            {
                if (rules.All(x => x.IsSatisfied(update)))
                {
                    sum += update[update.Length / 2];
                }
            }

            return sum.ToString();
        }

        private static string GetCorrectedIncorrectUpdateSum(List<PageOrderingRule> rules, List<int[]> pageUpdates)
        {
            int sum = 0;
            foreach (var update in pageUpdates)
            {
                bool wasIncorrect = false;
                while (!rules.All(x => x.IsSatisfied(update)))
                {
                    wasIncorrect = true;
                    foreach (var rule in rules)
                    {
                        if (rule.IsSatisfied(update))
                        {
                            continue;
                        }

                        var first = Array.IndexOf(update, rule.First);
                        var second = Array.IndexOf(update, rule.Second);
                        (update[first], update[second]) = (update[second], update[first]);
                    }
                }

                if (wasIncorrect)
                {
                    sum += update[update.Length / 2];
                }
            }

            return sum.ToString();
        }

        private void GetRulesAndUpdates(out List<PageOrderingRule> rules, out List<int[]> pageUpdates)
        {
            rules = new List<PageOrderingRule>();
            pageUpdates = new List<int[]>();
            foreach (var line in File.ReadLines(DataFilename))
            {
                if (_ruleRegex.IsMatch(line))
                {
                    string[] split = line.Split('|');
                    rules.Add(new PageOrderingRule(int.Parse(split[0]), int.Parse(split[1])));
                }
                else if (_updateRegex.IsMatch(line))
                {
                    pageUpdates.Add(line.Split(',').Select(int.Parse).ToArray());
                }
            }
        }

        private class PageOrderingRule
        {
            public PageOrderingRule(int first, int second)
            {
                First = first;
                Second = second;
            }

            public int First { get; }

            public int Second { get; }

            public bool IsSatisfied(int[] pageUpdates)
            {
                var first = Array.IndexOf(pageUpdates, First);
                var second = Array.IndexOf(pageUpdates, Second);

                return first == -1 || second == -1 || first < second;
            }
        }
    }
}