#include <vector>
#include <string>
#include <deque>
using namespace std;

class TextJustificator // LeetCode Q.68.
{
private:
    deque<string> queue;

    string formSentence(int charsCount, int maxWidth, bool leftJustify)
    {
        string intervalSpaces = "";
        int intervalsCount = queue.size() - 1, modulo = 0;

        if (intervalsCount > 0 && !leftJustify)
        {
            int quotient = (maxWidth - charsCount) / intervalsCount;
            for (int num = 0; num < quotient; num++)
                intervalSpaces += " ";

            modulo = (maxWidth - charsCount) % intervalsCount;
        }

        string sentence = "";

        for (int idx = 0; idx < queue.size(); idx++)
        {
            sentence += queue[idx];

            if (idx < queue.size() - 1)
            { // Not the last word.
                if (leftJustify)
                {
                    sentence += " "; // Left-justification.
                    continue;
                }

                sentence += intervalSpaces; // Right-justification.
                if (modulo > idx)
                    sentence += " "; // Need to pad extra space at left intervals.
            }
        }
        queue.clear(); // Reset for future usage.

        // Right end padding only runs for left-justification.
        while (sentence.size() < maxWidth)
            sentence += " ";
        return sentence;
    }

public:
    vector<string> justifyText(vector<string> &words, int maxWidth)
    {
        vector<string> justifiedSentences;
        int charsCount = 0; // Characters only. Not counting interval spaces.

        for (auto word : words)
        {
            // Current sentence is finalized.
            if (charsCount + queue.size() - 1 + word.size() + 1 > maxWidth)
            {
                string sentence = formSentence(charsCount, maxWidth, false);
                justifiedSentences.push_back(sentence);
                charsCount -= charsCount; // Reset for the next sentence.
            }

            queue.push_back(word);
            charsCount += word.size();
        }

        // Deal with last sentence. Last sentence must be left-justified.
        string sentence = formSentence(charsCount, maxWidth, true);
        justifiedSentences.push_back(sentence);
        return justifiedSentences;
    }
};