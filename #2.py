def interactive_quiz():
    questions = [
        {"question": "1. What shape does not have any sides and corners.?", "answer": "Circle"},
        {"question": "2. What is 2 + 2?", "answer": "4"},
        {"question": "3. What is the largest planet in our solar system?", "answer": "Jupiter"},
        {"question": "4. How many legs does a spider have?", "answer": "8"},
        {"question": "5. What galaxy do we live in?", "answer": "Milky Way"},
        {"question": "6. How many sides does a triangle have?", "answer": "3"},
        {"question": "7. Who painted the Mona Lisa?", "answer": "Leonardo da Vinci"},
        {"question": "8. What is the square root of 64?", "answer": "8"},
        {"question": "9. What is the chemical symbol for gold?", "answer": "Au"},
        {"question": "10. How many lives are cats said to have?", "answer": "9"},
        {"question": "11. Which animal is known as the 'Ship of the Desert?", "answer": "Camel"},
        {"question": "12. What is 4 + 4?", "answer": "8"},
        {"question": "13. How many days are there in a week?", "answer": "7"},
        {"question": "14. How many hours are there in a day?", "answer": "24"},
        {"question": "15. How many letters are there in the English alphabet?", "answer": "26"},
        {"question": "16. Rainbow consist of how many colours?", "answer": "7"},
        {"question": "17. How many days are there in a year?", "answer": "365"},
        {"question": "18. How many minutes are there in an hour?", "answer": "60"},
        {"question": "19. How many seconds make one hour?", "answer": "3600"},
        {"question": "20. Baby frog is known as.......", "answer": "tadpole"},
        {"question": "21. How many consonants are there in the English alphabet?", "answer": "21"},
        {"question": "22. How many vowels are there in the English?", "answer": "5"},
        {"question": "23. Which animal is known as the king of the jungle?", "answer": "Lion"},
        {"question": "24. Name the National bird of Philippines?", "answer": "Philippine Eagle"},
        {"question": "25. Name the National animal of Philippines?", "answer": "Carabao"},
        {"question": "26. What is the National Anthem of Philippines?", "answer": "Lupang Hinirang"},
        {"question": "27. Name the national flower of Philippines?", "answer": "Sampaguita"},
        {"question": "28. Name the National fruit of Philippines?", "answer": "Mango"},
        {"question": "29. What is the National leaf of Philippines?", "answer": "Anahaw"},
        {"question": "30. What is the National tree of Philippines?", "answer": "Narra"},
        {"question": "31. Name the National sport of Philippines?", "answer": "Arnis"},
        {"question": "32. Name the National national hero of the Philippines?", "answer": "Jose Rizal"},
        {"question": "33. Name the National gem of Philippines?", "answer": "Pearl"},
        {"question": "34. Name the National language of the Philippines?", "answer": "Filipino"},
        {"question": "35. What is the capital of Philippines?", "answer": "Manila"},
        {"question": "36. Name the biggest continent in the world?", "answer": "ASia"},
        {"question": "37. How many continents are there in the world?", "answer": "7"},
        {"question": "38. Which is the smallest month of the year?", "answer": "Frebuary"},
        {"question": "39. Name the house made of ice?", "answer": "Igloo"},
        {"question": "40. What is 6 x 6?", "answer": "36"},
        {"question": "41. What is the capital of France?", "answer": "Paris"},
        {"question": "43. What is the chemical formula for water?", "answer": "H2O"},
        {"question": "44. In what year did World War II begin?", "answer": "1939"},
        {"question": "45. What is the tallest mountain in the world?", "answer": "Mount Everest"},
        {"question": "46. How many sides does a hexagon have?", "answer": "6"},
        {"question": "47. What is the currency of Japan?", "answer": "Japanese Yen"},
        {"question": "48. Who wrote the play Hamlet?", "answer": "William Shakespeare"},
        {"question": "49. What is the process of turning a liquid into a gas called?", "answer": "Evaporation"},
        {"question": "50. What is the scientific name for humans?", "answer": "Homo sapiens"},
        {"question": "51. What is the capital of Australia?", "answer": "Canberra"},
        {"question": "52. What is the largest ocean on Earth?", "answer": "Pacific Ocean"},
        {"question": "53. What does CPU stand for?", "answer": "Central Processing Unit"},
        {"question": "54. What is the square root of 25?", "answer": "5"},
        {"question": "55. What is the chemical symbol for silver?", "answer": "Ag"},
        {"question": "56. What is the capital of Germany?", "answer": "Berlin"},
        {"question": "57. What is the tallest building in the world?", "answer": "Burj Khalifa"},
        {"question": "58. What is the scientific study of insects called?", "answer": "Entomology"},
        {"question": "59. What is the largest desert in the world?", "answer": "Sahara Desert"},
        {"question": "50. What is the capital of Italy?", "answer": "Rome"},
        {"question": "51. What is the scientific study of weather called?", "answer": "Meteorology"},
        {"question": "52. What is the largest freshwater lake by volume?", "answer": "Lake Baikal"},
        {"question": "53. What is the capital of Canada?", "answer": "Ottawa"},
        {"question": "54. What is the scientific study of animals called?", "answer": "Zoology"},
        {"question": "55. What is the longest river in the world?", "answer": "Nile River"},
        {"question": "56. What is the capital of Spain?", "answer": "Madrid"},
        {"question": "57. What is the scientific study of plants called?", "answer": "Botany"},
        {"question": "58. What is the hottest planet in our solar system?", "answer": "Venus"},
        {"question": "59. What is the capital of India?", "answer": "New Delhi"},
        {"question": "60. What is the scientific study of the Earth called?", "answer": "Geology"},
        {"question": "61. What is the coldest place on Earth?", "answer": "Vostok Station, Antarctica"},
        {"question": "62. What is the capital of China?", "answer": "Beijing"},
        {"question": "63. What is the scientific study of stars and galaxies called?", "answer": "Astronomy"},
        {"question": "64. What is the world's most populous country?", "answer": "China"},
        {"question": "65. What is the capital of Brazil?", "answer": "Brasília"},
        {"question": "66. How many bones are there in the human adult body?", "answer": "206 (approximately)"},
        {"question": "67. What is the capital of the United States?", "answer": "Washington D.C."},
        {"question": "68. What is the scientific study of the human body called?", "answer": "Anatomy"},
        {"question": "69. What is the world's second most populous country?", "answer": "India"},
        {"question": "70. What is the capital of Mexico?", "answer": "Mexico City"},
        {"question": "71. What is the scientific study of machines called?", "answer": "Mechanics"},
        {"question": "72. What is the world's third most populous country?", "answer": "United States"},
        {"question": "73. What is the capital of Russia?", "answer": "Moscow"},
        {"question": "74. What is the scientific name for a cat?", "answer": "Felis catus"},
        {"question": "75. What is the process of turning a gas into a liquid called?", "answer": "Condensation"},
        {"question": "76. How many degrees are in a circle?", "answer": "360 degrees"},
        {"question": "77. What is the capital of Italy?", "answer": "Rome"},
        {"question": "78. What is the chemical element with the atomic number 8?", "answer": "Oxygen (O)"},
        {"question": "79. What is the third planet from the Sun?", "answer": "Earth"},
        {"question": "80. What is the smallest country in the world?", "answer": "Vatican City"},
        {"question": "81. What is the process of turning a solid into a liquid called?", "answer": "Melting"},
        {"question": "82. What is the name of the largest search engine in the world?", "answer": "Google"},
        {"question": "83. In what year did World War I begin?", "answer": "1918"},
        {"question": "84. What is the capital of India?", "answer": "New Delhi"},
        {"question": "85. What is the process of separating a mixture into its component parts called?", "answer": "Fractionation"},
        {"question": "86. What is the scientific name for a human brain?", "answer": "Cerebrum"},
        {"question": "87. Who invented the light bulb?", "answer": "Thomas Edison"},
        {"question": "88. What is the capital city of Japan?", "answer": "Tokyo"},
        {"question": "89. How many bones are there in the human body?", "answer": "206"},
        {"question": "90. How many years are in a millennium?", "answer": "1000"},
        {"question": "91. What is the largest animal in the world?", "answer": "Blue whale"},
        {"question": "92. How many teaspoons are in a tablespoon?", "answer": "3"},
        {"question": "93. Who discovered America?", "answer": "Christopher Columbus"},
        {"question": "94. How many players are there on a soccer team?", "answer": "11"},
        {"question": "95. How many months have 31 days?", "answer": "7"},
        {"question": "96. What is the tallest tree in the world?", "answer": "Hyperion"},
        {"question": "97. Who was the first President of the United States?", "answer": "George Washington"},
        {"question": "49. How many legs does a butterfly have?", "answer": "6"},
        {"question": "50. What is the chemical symbol for carbon?", "answer": "C"},
        {"question": "62. How many years are there in a leap year?", "answer": "366"},

    ]

    score = 0

    for i in questions:
        user_answer = input(i["question"] + " Enter your answer: ")
        if user_answer.lower() == i["answer"].lower():
            score += 1

    print(f"Your score is {score} out of {len(questions)}")

if __name__ == "__main__":
    interactive_quiz()