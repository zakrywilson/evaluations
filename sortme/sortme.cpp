/*
 * Zach Wilson
 * custom-sort.cpp
 */


#include <iostream>
#include <string>
#include <sstream>
#include <map>
#include <vector>


const int NUMBER_LINE = 0;
const int CUSTOM_ORDER_LINE = 1;
const int ITEM_LINE = 2;


/*
 * Holds the custom order for sorting
 */
std::map<char, unsigned> order;


/*
 * Holds the strings to be sorted
 */
std::vector<std::string> things;


/*
 * Exception for invalid input from command line
 */
struct invalid_input {
  std::string input;
  invalid_input(std::string in) : input(in) {}
};


/*
 * Prints the vector
 */
void print_vector() {
  for (int item = 0; item < things.size(); ++item) {
    std::cout << things[item] << std::endl;
  }
}


/*
 * Determines whether the strings need to be swapped - 
 * whether the first string is larger than the second.
 *
 * return: true if the strings need to be swapped
 */
bool needs_swapped(std::string string1, 
                               std::string string2) {

  // Comparing each letter with respect to custom order
  for (int index = 0;
       index < string1.length() && index < string2.length();
       ++index) {

    // Get the new value for the letter being compared
    unsigned first = order.at(toupper(string1[index]));
    unsigned second = order.at(toupper(string2[index]));

    if (first > second) return true; 
    else if (first < second) return false; 
  }

  // Tie breaker: shorter word stays on top
  if (string1.length() < string2.length()) {
    return false;
  }

  // Otherwise, we'll swap
  return true;
}


/*
 * Implements reverse bubble sort for the vector of strings
 * based on the order the user specified.
 */
void sort() {

  std::string first, second, temp;
  int counter = 1;

  for (int outter = 0; outter < things.size() - 1; ++outter, ++counter) {

    for (int item = 0; item < (things.size() - counter); ++item) {
      
      // Get the two strings to compare
      first = things[item];
      second = things[item + 1];
      
      // Check if swapping needs to occur
      if (needs_swapped(first, second)) {
        
        // Do the swap
        things[item] = second;
        things[item + 1] = first;
      } 
    }
  }
}


/*
 * Converts a string to an integer
 */
int convert(std::string text) {
  int val;
  std::stringstream ss(text);
  if (!(ss >> val)) throw invalid_input(text);
  return val;
}


/*
 * Just runs the program
 */
int main() {
  
  std::string line;
  int location, expected_number_of_items, counter, year = 0;

  while (std::cin) {

    // read in line
    std::cin >> line;

    // First line is a number
    if (location == NUMBER_LINE) {
      if (line == "0") break; 
      expected_number_of_items = convert(line);
      location++;
    } 
    
    // Second line is the new order
    else if (location == CUSTOM_ORDER_LINE) {
      
      // Load up the map for the customized order
      for (unsigned letter = 0; letter < line.length(); ++letter) {
        order.insert(std::make_pair((char) line[letter], letter));
      }

      location++;
    } 
    
    // Following lines are items to sort
    else if (location == ITEM_LINE) {

      things.push_back(line);
      ++counter;

      // Check if we have all items, if so sort them
      if (counter >= expected_number_of_items) {

        // Do the thing
        sort();
        std::cout << "year " << ++year << std::endl;
        print_vector();

        // Resetting everything
        location = 0;
        counter = 0;
        things.clear();
        order.clear();
      }
    }
  }
  
  return 0;
}
