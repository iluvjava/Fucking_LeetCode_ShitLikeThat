## Coellectors.groupBy

* This is a funcition that transfers a stream of data into a map.

* The method that got applied to the stream of data is: `java.stream.collect()`

* `.stream()` is the method that pulls out a stream out from the List<T>, or collections in general.

* `.stream().collect(?)`, apply the collect function to the stream of data, the collect function will take in the
follwoing parameters:

  * Takes in:
    * An Instance of  ? = `Collector<? super T, A, R>`

  * Output:
    * a output of type R, that specified in the context of the generic type of the thing we are looking at.

* java.util.stream.Collectors()

* `.stream().collect(?, ?, ?)`

* Collector:
  * This is an interface, representing the the common operations applied to a list of elements, in the array, and it
  reduces it to a value, e.g the count, the average, or shit like that.
  * A collector is essentially the abstraction of a sequence of operations.

### Collectors.groupby

```
public static <T,K,D,A,M extends Map<K,D>> Collector<T,?,M> groupingBy (
  Function<? super T,? extends K> classifier,
  Supplier<M> mapFactory,
  Collector<? super T,A,D> downstream)
```

* Let me explain as best as I can:

* The classifier takes in a element from the sequence, reduce it to a value that represents the element, which
is also the key for classifying the elements from the sequence.
  * It is a function that can be described as (a) ==> (b), univariate.

* The supplier is just a new instance of the map factory...
  * something TreeMap::new
  * The `Suppler<M>` just return some thing and then it dies, that is basically is, then TreeMap::new is a
  supplier, which indicates the constructor of the Type: TreeMap, and it will return a new instance of the
  TreeMap for holding the elements from the stream when grouped.

* Collection is the final step of the reduction.
  * used as `Collectors.mapping(fxn1, groupingFxn)`, the first is a bijective transform on the elements in the
  values, and the second one is function that reduce the whole group to something, some of the example inclues:
    * Collectors.asList(): Reduce the values into a list of stuff.
    * Collectors.summingInt(): if the values are ints, then this will sum them up.
    * etc, just read about the factor methods in the Collectors class.

### String Functionalities Associated with Maps

* The Compute Method:

  ```
    default V compute(K key, BiFunction<? super K,? super V,? extends V> remappingFunction)
  ```

  * It attempts to recompte the keys and values inside the map in a streamlined fasion.
    * foreach key, we try to recompute the key values pair for it.
    * This is doing it for ONE specific key, it's like an... update..., super easy stuff in python and C# with 
    indexer but is like this in java.

  * This function is equivalent to the following codes:

  ```
    V oldValue = map.get(key);
    V newValue = remappingFunction.apply(key, oldValue);
    if (oldValue != null ) {
      if (newValue != null)
          map.put(key, newValue);
      else
          map.remove(key);
    } else {
      if (newValue != null)
          map.put(key, newValue);
      else
          return null;
    }
  ```

  * Summary:
    * Compute the new value using the old kvpairs.
    * Assuming old value is not null, if the new value is also not null, then the key get the new value assigned to it,
    else the new value is null, then the old key will be deleted from the map.
    * Assuming the old value is null, if the new value is not null, then the new value will become the value of the
    old key, else the old value still maps to **null**.

  * Updating the the keyvalue pair, and using the null type to get rid of the old keys. 