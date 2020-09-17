/**
 * Here we are going to demonstrate some of the usage of the groupby 
 * functionalities in java stream. 
 */
import java.util.*;
import java.util.stream.Collectors;

class GroupbyDemo 
{
    public static void main(String[] args)
    {
        List<BlogPost> posts = new LinkedList<>();
        Map<BlogPostType, List<BlogPost>> postsPerType = posts.stream().collect(Collectors.groupingBy(e -> e.type));
        
    }


}

/**
 * A basic example class that has multiple useful attributes for 
 * demonstration 
 */
class BlogPost {
    String title;
    String author;
    BlogPostType type;
    int likes;
}

enum BlogPostType {
    NEWS,
    REVIEW,
    GUIDE
}

class Tuple {
    BlogPostType type;
    String author;
}