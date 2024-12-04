using AdventOfCode._2024.Library;

namespace AdventOfCode._2024._04
{
    internal class WordSearchSolver : APuzzle
    {
        private const string WordOne = "XMAS";
        private readonly Func<int, int>[] Moves = [x => x, x => x + 1, x => x - 1];

        public WordSearchSolver(string dataFilename, Part part) : base(dataFilename, part)
        { }

        public override string GetAnswer()
        {
            return Part switch
            {
                Part.One => CountWord().ToString(),
                Part.Two => CountXWord().ToString(),
                _ => throw new NotSupportedException()
            };
        }

        private int CountXWord()
        {
            char[][] wordSearch = File.ReadLines(DataFilename).Select(x => x.ToCharArray()).ToArray();
            int count = 0;

            for (int y = 1; y < wordSearch.Length - 1; y++)
            {
                for (int x = 1; x < wordSearch[y].Length - 1; x++)
                {
                    if (wordSearch[y][x] != 'A')
                    {
                        continue;
                    }

                    if (Check(x, y, 'M', 'S', 'M', 'S')
                        || Check(x, y, 'M', 'S', 'S', 'M')
                        || Check(x, y, 'S', 'M', 'M', 'S')
                        || Check(x, y, 'S', 'M', 'S', 'M'))
                    {
                        count++;
                    }
                }
            }

            return count;

            bool Check(int x, int y, char posPos, char negNeg, char negPos, char posNeg)
            {
                return wordSearch[y + 1][x + 1] == posPos
                    && wordSearch[y - 1][x - 1] == negNeg
                    && wordSearch[y - 1][x + 1] == negPos
                    && wordSearch[y + 1][x - 1] == posNeg;
            }
        }

        private int CountWord()
        {
            char[][] wordSearch = File.ReadLines(DataFilename).Select(x => x.ToCharArray()).ToArray();
            int count = 0;

            for (int y = 0; y < wordSearch.Length; y++)
            {
                for (int x = 0; x < wordSearch[y].Length; x++)
                {
                    foreach (var xMove in Moves)
                    {
                        foreach (var yMove in Moves)
                        {
                            if (Search(x, xMove, y, yMove))
                            {
                                count++;
                            }
                        }
                    }
                }
            }

            return count;

            bool Search(int x, Func<int, int> xMove, int y, Func<int, int> yMove)
            {
                short i = 0;
                while (i < WordOne.Length)
                {
                    if (y >= wordSearch.Length || y < 0 || x >= wordSearch[y].Length || x < 0)
                    {
                        return false;
                    }

                    if (wordSearch[y][x] != WordOne[i])
                    {
                        return false;
                    }

                    x = xMove(x);
                    y = yMove(y);
                    i++;
                }

                return true;
            }
        }
    }
}