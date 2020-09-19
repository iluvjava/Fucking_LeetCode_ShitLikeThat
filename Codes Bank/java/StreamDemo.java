import java.util.*;
import java.util.Map.Entry;
import java.util.function.Function;
import java.util.stream.*;


/**
 *   This is gonna be another demo for the method.
 */
public class StreamDemo {
    
    public static void main(final String[] args)
    {
        // Frequency Mapping Demo
        {
            final char[] TestString = "this is some dope shit".toCharArray();
            final List<Character> Boxed = new LinkedList<>();
            for (final char C : TestString) Boxed.add(C);
            final TreeMap<Character, Integer> Frmap = QuickCounter(Boxed);
            System.out.println(Frmap);
        }
        
        // Edges list to Adjacency list demo
        {
            final int[][] Edges = new int[][]{
                new int[]{1, 2}, 
                new int[]{2, 3}, 
                new int[]{3, 1},
            };  // A circled triangle

            System.out.println(ConvertToAdjacencyList(Edges, true));
            System.out.println(ConvertToAdjacencyList(Edges, false));
        }

        // Getting the top k most frequence symbols from the sequence. 
        {
            char[] Clist = "aaabbccdefg".toCharArray();
            LinkedList<Character> Boxed = new LinkedList<>();
            for (char C : Clist) Boxed.add(C);
            
            // TopKMostFrequent(Boxed, 2);
            
            List<Character> Boxed2 = IntStream.range(0, Clist.length)
                                              .mapToObj((i) -> (Character)Clist[i])
                                              .collect(Collectors.toList());
            System.out.println(Boxed2);
            System.out.println(TopKMostFrequent(Boxed2, 2));
        }

        // Testing Map reversed.
        {
            char[] Sequence = ("Ok, Amazon interviews can be very anonying and they test you on " + 
            "core Leadership Principles. ").toCharArray();
            List<Character> CharList = IntStream
                    .range(0, Sequence.length).mapToObj(I -> Sequence[I])
                    .collect(Collectors.toList());
            TreeMap<Character, Integer> Fmap = QuickCounter(CharList);
            Map<Integer, Character> MapReversed = MapReversed(Fmap);
            System.out.println(MapReversed);
        }
    }

    /**
     * Method creates a fast conversion from a sequence of generic type to a map that can be a 
     * Sorted Multiset of the input sequence. 
     */
    public static <T extends Comparable> TreeMap<T, Integer> QuickCounter(final List<T> sequence)
    {
        TreeMap<T, Integer> Res = sequence.stream().
                collect (
                            Collectors.groupingBy (
                            Function.identity(),  // The element itself as the classifer
                            TreeMap::new,  // Create the new map as a Treemap
                            Collectors.summingInt(e -> 1)  // e -> 1 maps element in the list of values into a list of 1, 
                            // and then collectors job is to sum them all up. 
                    )
            );
        return Res;
    }

    public static <T extends Comparable> List<T> TopKMostFrequent(List<T> sequence, int k)
    {
        TreeMap<T, Integer> Fmap = QuickCounter(sequence);

        SortedSet<Integer> TopK = new TreeSet<>();
        {
            for (int I : Fmap.values())
            {
                if (TopK.size() < k) TopK.add(I);
                else 
                {
                    if (I > TopK.last())
                    {
                        TopK.remove(TopK.last());
                        TopK.add(I);
                    }
                }
            }
        }
        System.out.println(TopK);
        List<T> TopKeys = Fmap.keySet()
                    .stream()
                    .filter(key -> Fmap.get(key) >= TopK.first())
                    .collect(Collectors.toList());
        return TopKeys;
    }

    /**
     *  Given a tuple of edges in a list, were each integers are representing a vertex in the graph,
     *  this function will convert the list of edges into a adjacency list, which represents the graph. 
     * @param edges
     * @param directed
     * @return
     *  The adjacency list of the graph.
     */
    public static TreeMap<Integer, List<Integer>> ConvertToAdjacencyList(final int[][] edges, final boolean directed)
    {
        final List<int[]> Edges = Arrays.asList(edges);
        return ConvertToAdjacencyList(Edges, directed);
    }

    /**
     * 
     * @param edges
     * @param directed
     * @return
     */
    public static TreeMap<Integer, List<Integer>> ConvertToAdjacencyList(List<int[]> edges, final boolean directed)
    {
        if (!directed)
        {
            // reverse all the edges and then add them back. 
            final List<int[]> EdgesReversed = new LinkedList<>();
            for (final int[] Tuple : edges)
            {
                EdgesReversed.add(new int[]{Tuple[1], Tuple[0]});
            }
            EdgesReversed.addAll(new LinkedList<int[]>(edges));
            edges = EdgesReversed;
        }

        final TreeMap<Integer, List<Integer>> AdjList = edges.stream().collect (
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


    /**
     * Map the values to groups of keys. 
     * @param <K>
     * @param <V>
     * @param map
     * @return
     */
    public static <K, V> Map<V, K> MapReversed(Map<K, V> map)
    {
        // Map split it to tuples list
        List<Entry<K, V>> Kvp = map.entrySet().stream().collect(Collectors.toList());
        Map<Object, List<Object>> Reversed = Kvp.stream().collect(
            Collectors.groupingBy(
                (e) -> e.getValue(),
                HashMap::new, 
                Collectors.mapping(e -> e.getKey(), Collectors.toList())
            )
        ); // The generic information is lost. 

        return (Map<V, K>) Reversed;
    }

    public static double VectorDot(double[] v1, double[] v2)
    {
        return IntStream
                .range(0, Math.min(v1.length, v2.length))
                .mapToDouble(I -> v1[I]*v2[I]).sum();
    }

}
