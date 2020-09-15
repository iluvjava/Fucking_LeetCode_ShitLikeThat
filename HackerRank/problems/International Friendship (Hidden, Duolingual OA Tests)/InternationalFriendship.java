package Duolingo;

import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

/**
 Simple two-tuple class representing that "person1" and "person2"
 are friends.
 */
class Friendship {
    public String person1;
    public String person2;

    public Friendship(String person1, String person2) {
        this.person1 = person1;
        this.person2 = person2;
    }
}

/**
 Wrapper class for the results that bestLanguage is expected to return.
 */
class BestLanguageResult {
    public String language;
    public int numLearners;

    public BestLanguageResult(String language, int numLearners) {
        this.language = language;
        this.numLearners = numLearners;
    }
}


class Result {

    /**
     * Complete the 'bestLanguage' function below.
     *
     * @param languages  A list of the languages to consider
     * @param people  A mapping from the names of people to the set of languages they speak
     * @param friends  A list of Friendship objects that represent that each represent
    that the two named individuals are friends.
     * @return  A BestLanguageResult object containing the best language and the number
    of individuals that have to learn that language.
     */
    public static BestLanguageResult bestLanguage(List<String> languages,
                                                  Map<String, Set<String>> people,
                                                  List<Friendship> friends) {

        // Replace this line with code to return the actual best language
        return new BestLanguageResult(languages.get(0), 1);
    }

}

public class InternationalFriendship {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int languagesCount = Integer.parseInt(bufferedReader.readLine().trim());

        List<String> languages = IntStream.range(0, languagesCount).mapToObj(i -> {
            try {
                return bufferedReader.readLine();
            } catch (IOException ex) {
                throw new RuntimeException(ex);
            }
        })
                                          .collect(toList());

        int peopleCount = Integer.parseInt(bufferedReader.readLine().trim());
        Map<String, Set<String>> peopleToLanguages = new HashMap<>(peopleCount);
        for (int i=0; i<peopleCount; i++) {
            String line;
            try {
                line = bufferedReader.readLine();
                List<String> components = Arrays.asList(line.split(","));
                String name = components.get(0);
                peopleToLanguages.put(name, new HashSet<>(components.subList(1, components.size())));
            } catch (IOException ex) {
                throw new RuntimeException(ex);
            }
        }

        int friendCount = Integer.parseInt(bufferedReader.readLine().trim());
        List<Friendship> friends = new ArrayList<>();
        for (int i=0; i<friendCount; i++) {
            String line;
            try {
                line = bufferedReader.readLine();
                String[] components = line.split(",");
                friends.add(new Friendship(components[0], components[1]));
            } catch (IOException ex) {
                throw new RuntimeException(ex);
            }
        }

        BestLanguageResult result = Result.bestLanguage(languages, peopleToLanguages, friends);

        bufferedWriter.write(String.format("%s,%d", result.language, result.numLearners));
        bufferedWriter.newLine();

        bufferedReader.close();
        bufferedWriter.close();
    }
}
