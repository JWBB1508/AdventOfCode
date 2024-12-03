namespace AdventOfCode._2024.Library
{
    internal class AoCMath
    {
        // https://stackoverflow.com/a/20824923
        public static long Gcf(long a, long b)
        {
            while (b != 0)
            {
                long temp = b;
                b = a % b;
                a = temp;
            }
            return a;
        }

        // https://stackoverflow.com/a/20824923
        public static long Lcm(long a, long b)
        {
            return a / Gcf(a, b) * b;
        }
    }
}