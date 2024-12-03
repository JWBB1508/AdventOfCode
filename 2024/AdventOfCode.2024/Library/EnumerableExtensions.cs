namespace AdventOfCode._2024.Library
{
    internal static class EnumerableExtensions
    {
        public static IEnumerable<IList<string>> Split(this IEnumerable<string> maps, Func<string, bool> splitter)
        {
            using var enumerator = maps.GetEnumerator();
            if (!enumerator.MoveNext())
            {
                yield break;
            }

            var group = new List<string> { enumerator.Current };
            while (enumerator.MoveNext())
            {
                var next = enumerator.Current;
                if (!splitter(next))
                {
                    group.Add(next);
                }
                else
                {
                    yield return group;
                    group = new List<string>();
                }
            }

            yield return group;
        }
    }
}