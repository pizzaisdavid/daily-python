#include <vector>
#include <string>
#include <algorithm>

using namespace std;

bool is_item_in_vector(vector<string> sequence, string item) {
    return find(sequence.begin(), sequence.end(), item) != sequence.end();
}
