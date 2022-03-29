# text-mining

Please read the [instructions](instructions.md).

Reflection
For this assignment, I compared two online books from the website called Project Gutenberg. To analyze those two books, I used Word Frequencies, Natural Language Processing, and Text Similarity. The goal of this project is to find out the similarity between the two books and form the whole project in a relatively clean format of data. 

For the coding part, instead of writing the code in a larger function, I chose to break them up into small pieces. I wrote different functions to make them look clearer and easier for me to use in the main function at the end. Separate all the code into different small functions, it also allows me to be more flexible when I call the function in the main since I can make more small changes in the end.

The biggest challenge that I met during the process it to determine whether to get rid of the word that is meaningless before I count them or after I have put the word and the count in a dictionary. In the end, I decided to make the dictionary first, then eliminate the meaningless word and insert the top 10 meaningful words into a new dictionary. The reason I chose to do it this way is that I remember that we just finished a similar project to keep the words that we want to keep according to another dictionary of the word that we would like to eliminate, which is the "subtract" function we wrote for text_process assignment. I think it is more convenient if I can use the function that I have written before. 

The interesting thing that I have found during the analysis process is that other than words like the, a, will, and so on, the most frequent word in both books are the name of the books. Moreover, the two books have some same high frequent words. Based on the words that are used in the book, we can somehow tell that both books are telling stories. Moreover, based on the adjectives in the books, we can tell that both books are telling similar types of stories.

Moreover, I also did the nltk and thefuzzy test to learn more about the two books. When we set the two book and compare them, the result shows that the similarity reaches 89 which shows that the words that were used to write these two books are highly similar. Besides, the ntlk shows that text1 used slightly more positive words than text2, and text2 used slightly more negative words than text1. 

I think the whole process went pretty smoothly. The challenge that I met during this assignment is that I had trouble using the packages I have downloaded. If more time is given, I think I would spend more time choosing the data source. I think I learned how to use different tools from the website, and also how to organize the code more clearly. 