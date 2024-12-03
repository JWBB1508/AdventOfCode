using AdventOfCode._2024.Library;

namespace AdventOfCode._2024._01
{
    internal class ListDistanceFinder(string dataFilename, Part part) : APuzzle(dataFilename, part)
    {
        public override string GetAnswer()
        {
            (var leftList, var rightList) = GetSortedLists();

            return Part switch
            {
                Part.One => GetListDistance(leftList, rightList).ToString(),
                Part.Two => GetListSimilarity(leftList, rightList).ToString(),
                _ => throw new ArgumentOutOfRangeException(nameof(Part), Part, "Unsupported Part"),
            };
        }

        private (List<int> leftList, List<int> rightList) GetSortedLists()
        {
            var leftList = new List<int>();
            var rightList = new List<int>();

            var lines = File.ReadLines(DataFilename);
            foreach (var line in lines)
            {
                var values = line.Split().Where(x => !string.IsNullOrWhiteSpace(x)).ToArray();
                leftList.Add(int.Parse(values[0]));
                rightList.Add(int.Parse(values[1]));
            }

            leftList.Sort();
            rightList.Sort();

            return (leftList, rightList);
        }

        private long GetListDistance(List<int> leftList, List<int> rightList)
        {
            return leftList.Zip(rightList).Sum(x => Math.Abs(x.First - x.Second));
        }

        private long GetListSimilarity(List<int> leftList, List<int> rightList)
        {
            var score = 0;
            foreach (var x in leftList)
            {
                score += x * rightList.Count(y => y == x);
            }

            return score;
        }
    }
}
