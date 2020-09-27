import java.util.Iterator;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.Stack;
import java.util.TreeMap;
import java.util.TreeSet;
import java.util.stream.Collectors;
import java.util.stream.IntStream;
import java.lang.System;

/**
 * A trie class better querying from a set of strings. * This is not token
 * based, it's string based and each token is the character.
 *  * Characters focused Trie, this is a tree. 
 *  * For each trie, we can query by one character and then look for another Trie within the current Trie.
 *  * This is not going to support sequence deletion for the simplicity 
 *  * Sequences long than 3000 characters are banned from this data structure because of recursive depths.
 */
class Trie
{

    public static void main(String[] args)
    {
        {
            Trie TheTrie = new Trie();
            TheTrie.add("this");
            TheTrie.add("the");
            TheTrie.add("there");
            System.out.print(TheTrie.traverseFromRoot());
        }
    }

    protected Map<Character, Trie> ThisLayer;
    protected Set<Character> TerminatingCharacter = new TreeSet<Character>();  // there is a token that terminates right here with that character.

    protected Stack<Trie> TreeCursor;  // Trie that started with the given QueryPrefix. 

    protected String QueryPrefix = "";  // Only the root trie should have this field. 

    // public Trie()
    // {

    // }

    public void add(String sequence)
    {

        char[] CharArr = sequence.toCharArray();
        List<Character> CharList = IntStream.range(0, sequence.length())
                    .mapToObj((I)-> (Character)CharArr[I]).collect(Collectors.toList());
        add(CharList);
    }

    /**
     * Adds a new sequence of character to the Trie data structure.
     * @param sequence
     */
    public void add(List<Character> sequence)
    {
        if (sequence.size() == 0)return;
        if (sequence.size() > 3000) throw new RuntimeException();
        Iterator<Character> Itr = sequence.iterator();
        Trie NextTrie = this;
        while (Itr.hasNext())
        {
            Character TheChar = Itr.next();
            if 
            (
                NextTrie.ThisLayer == null 
                ||
                !NextTrie.ThisLayer.containsKey(TheChar)
            )
            {
                if (Itr.hasNext())
                NextTrie.appendCharacter(TheChar);
                else NextTrie.addLastCharacter(TheChar);
            }
            NextTrie = NextTrie.ThisLayer.get(TheChar);
        }
    }


    /**
     * Add a character, but this character is terminating one of the sequence.
     * @param c
     */
    public void addLastCharacter(char c)
    {
        if (!ThisLayer.containsKey(c))
        {
           appendCharacter(c);
        }
        TerminatingCharacter.add(c);
    }

    /**
     * Add just one character to the, it will delete all sub trie on that caracter too.
     * internal use and external use. 
     * @param c
     */
    public void appendCharacter(char c)
    {
        if (ThisLayer == null)
        ThisLayer = new TreeMap<>();
        ThisLayer.put(c, new Trie());
    }

    /**
     * Get the current query prefix from this tree. 
     * @return
     */
    public String currentQueryPrefix()
    {
        return QueryPrefix;
    }

    /**
     * And an additional character to the query string. 
     */
    public void addToQueryPrefix(Character c)
    {

    }

    public Set<String> traverseFromRoot()
    {
        Set<String> AllSequences = new TreeSet<>();
        traverseFromRoot(new StringBuilder(), AllSequences);
        return AllSequences;
    }

    /**
     *  Start traversing the current Trie, starting without any prefix.
     */
    protected void traverseFromRoot
    (
        StringBuilder stringPath, 
        Set<String> accumulator
    )
    {
        if (ThisLayer == null)
        {
            accumulator.add(stringPath.toString());
            return;
        }
        for (Map.Entry<Character, Trie> TheEntry : ThisLayer.entrySet())
        {
            Character C = TheEntry.getKey();
            Trie InnerTrie = TheEntry.getValue();
            stringPath.append(C);
            InnerTrie.traverseFromRoot(stringPath, accumulator);
            stringPath.deleteCharAt(stringPath.length() - 1);
        }
        return;
    }






    
}