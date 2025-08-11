#include <vector>
#include <string>
#include <deque>
using namespace std;

class TextJustificator
{ // LeetCode Q.68.
private:
    vector<string> formatted_texts;
    deque<string> queue;
    int max_width, queue_words_len = 0;

    void form_text(bool last_line)
    {
        int spaces = max_width - queue_words_len;
        int slots = queue.size() - 1;

        int spaces_per_slot = 1, extra_padded_slots = 0;
        if (slots > 0 && last_line == false)
        {
            spaces_per_slot = spaces / slots;
            extra_padded_slots += spaces % slots;
        }

        string text = "";
        for (int queue_idx = 0; queue_idx < queue.size(); queue_idx++)
        {
            text += queue[queue_idx];

            if (queue_idx < slots)
            { // Need to pad spaces after current word.
                text.append(spaces_per_slot, ' ');
                if (queue_idx < extra_padded_slots)
                    text.append(1, ' ');
            }
        }

        if (text.length() < max_width) // Rightmost spaces.
            text.append(max_width - text.length(), ' ');
        formatted_texts.push_back(text);

        queue.clear(); // Reset.
        queue_words_len -= queue_words_len;
    }

public:
    vector<string> justify_text(vector<string> &words, int width_limit)
    {
        max_width = width_limit;
        for (int word_idx = 0; word_idx < words.size(); word_idx++)
        {
            string word = words[word_idx];
            if (queue_words_len + word.length() + queue.size() > max_width)
                form_text(false);

            queue.push_back(word);
            queue_words_len += word.length();
            if (word_idx == words.size() - 1)
                form_text(true);
        }

        return formatted_texts;
    }
};