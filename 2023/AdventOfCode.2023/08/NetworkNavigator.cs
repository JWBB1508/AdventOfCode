using AdventOfCode._2023.Library;
using System.Text.RegularExpressions;

namespace AdventOfCode._2023._08
{
    internal class NetworkNavigator : APuzzle
    {
        public NetworkNavigator(string dataFilename, Part part)
            : base(dataFilename, part)
        { }

        public override string GetAnswer()
        {
            string[] lines = File.ReadAllLines(DataFilename);

            char[] directions = lines[0].ToCharArray();

            IDictionary<string, Node> nodes = lines
                .Skip(2)
                .Select(Node.FromData)
                .ToDictionary(x => x.Name);

            long steps = Part == Part.Two
                ? GetLcmOfNavigations(directions, nodes)
                : SingleNavigate(directions, nodes["AAA"], nodes);

            return steps.ToString();
        }

        private long SingleNavigate(
            char[] directions,
            Node start,
            IDictionary<string, Node> nodes)
        {
            int steps = 0;
            int index = 0;
            Node current = start;
            while ((Part == Part.One && current.Name != "ZZZ") || (Part == Part.Two && !current.Name.EndsWith('Z')))
            {
                steps++;

                if (directions[index] == 'L')
                {
                    current = nodes[current.Left];
                }
                else
                {
                    current = nodes[current.Right];
                }

                index = (index + 1) % directions.Length;
            }

            return steps;
        }

        // Brute force approach - untenable
        ////private static int ParallelNavigate(
        ////    char[] directions,
        ////    IDictionary<string, Node> nodes)
        ////{
        ////    Node[] currents = nodes
        ////        .Where(x => x.Key.EndsWith('A'))
        ////        .Select(x => x.Value)
        ////        .ToArray();
        ////    int steps = 0;
        ////    int index = 0;
        ////    while (!currents.All(x => x.Name.EndsWith('Z')))
        ////    {
        ////        steps++;

        ////        if (directions[index] == 'L')
        ////        {
        ////            Parallel.For(0, currents.Length, i => currents[i] = nodes[currents[i].Left]);
        ////        }
        ////        else
        ////        {
        ////            Parallel.For(0, currents.Length, i => currents[i] = nodes[currents[i].Right]);
        ////        }

        ////        index = (index + 1) % directions.Length;
        ////    }

        ////    return steps;
        ////}

        // LCM approach: discovered this was the 'correct' approach online (controversial, however!)
        private long GetLcmOfNavigations(char[] directions, IDictionary<string, Node> nodes)
        {
            Node[] currents = nodes
                .Where(x => x.Key.EndsWith('A'))
                .Select(x => x.Value)
                .ToArray();

            IList<long> steps = new List<long>();
            foreach (Node current in currents)
            {
                steps.Add(SingleNavigate(directions, current, nodes));
            }

            return steps.Aggregate((x, y) => AoCMath.Lcm(x, y));
        }


        private class Node
        {
            private Node(string name, string left, string right)
            {
                Name = name;
                Left = left;
                Right = right;
            }

            public string Name { get; }

            public string Left { get; }

            public string Right { get; }

            public static Node FromData(string data)
            {
                var match = Regex.Match(data, @"(\w+) = \((\w+), (\w+)\)");

                return new Node(
                    match.Groups[1].Value,
                    match.Groups[2].Value,
                    match.Groups[3].Value);
            }
        }
    }
}
