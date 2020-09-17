import java.util.*;
import java.util.function.Function;
import java.util.stream.*;

/**
 * This is gonna be another demo for the method.
 * 
 */
public class GroupbyDemo2 {
    
    public static void main(String[] args)
    {
        {
            char[] TestString = "this is some dope shit".toCharArray();
            List<Character> Boxed = new LinkedList<>();
            for (char C : TestString) Boxed.add(C);
            TreeMap<Character, Integer> Frmap = QuickCounter(Boxed);
            System.out.println(Frmap);
        }

        {
            int[][] Edges = new int[][]{
                new int[]{1, 2}, 
                new int[]{2, 3}, 
                new int[]{3, 1},
            };  // A circled triangle

            System.out.println(ConvertToAdjacencyList(Edges, true));
            System.out.println(ConvertToAdjacencyList(Edges, false));
        }
    }


    /**
     * Method creates a fast conversion from a sequence of generic type to a map that can be a 
     * Sorted Multiset of the input sequence. 
     */
    public static <T extends Comparable<T>> TreeMap<T, Integer> QuickCounter(List<T> sequence)
    {
        TreeMap<T, Integer> Res = sequence.stream().
            collect (
                Collectors.groupingBy (
                    Function.identity(),  // The element itself as the classifer
                    TreeMap::new,  // Create the new map as a Treemap
                    Collectors.mapping(e -> 1, Collectors.summingInt(e -> e))  // Map each of the element in the 
                    // grouped set to 1, and then reduce them by summing them up, which gives the frequency 
                    // of the element in the sequence. 
                )
            );
        return Res;
    }

    /**
     * Given a tuple of edges in a list, were each integers are representing a vertex in the graph,
     * this function will convert the list of edges into a adjacency list, which represents the graph. 
     * @param edges
     * @param directed
     * @return
     * The adjacency list of the graph. 
     */
    public static TreeMap<Integer, List<Integer>> ConvertToAdjacencyList(int[][] edges, boolean directed)
    {
        List<int[]> Edges = Arrays.asList(edges);
        return ConvertToAdjacencyList(Edges, directed);
    }

    /**
     * 
     * @param edges
     * @param directed
     * @return
     */
    public static TreeMap<Integer, List<Integer>> ConvertToAdjacencyList(List<int[]> edges, boolean directed)
    {
        if (!directed)
        {
            // reverse all the edges and then add them back. 
            List<int[]> EdgesReversed = new LinkedList<>();
            for (int[] Tuple : edges)
            {
                EdgesReversed.add(new int[]{Tuple[1], Tuple[0]});
            }
            EdgesReversed.addAll(new LinkedList<int[]>(edges));
            edges = EdgesReversed;
        }

        TreeMap<Integer, List<Integer>> AdjList = edges.stream().collect (
            Collectors.groupingBy(
                (e) -> e[0], 
                TreeMap::new,
                Collectors.mapping(
                        (e) -> e[1],
                        Collectors.toList()
                    )
            )
        );
        return AdjList;
    }

}


class Point {
    public int x;
    public int y;
    public Point (int x, int y)
    {
        this.x = x;
        this.y = y;
    }
}
