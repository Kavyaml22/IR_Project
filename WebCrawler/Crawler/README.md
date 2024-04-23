
# CS429 - IR Project Report 

#### Name: Kavya Muniyur Lakshminarayana
#### CWID: A20562801

 ## Web Based Search Engine

The project's structure and execution instructions are outlined in this README file, which is primarily divided into three parts.
 - Crawler
 - Indexer
 - Processor

## Abstract:

With the use of Scrapy, Scikit-Learn, and Flask, this project seeks to create a web document downloader, indexer, and query processor. The main goal is to build a comprehensive web content retrieval, indexing, and querying infrastructure.  The crawler retrieves web content in HTML format, TF-IDF representation and cosine similarity are used by the indexer to create an inverted index, the query processor processes free text searches and provides top k ranked results . 

#### - Summary:

A Crawler, Indexer, and  Processor are the three primary parts of the project that need to be developed. After initializing with a starting URL , the crawler retrieves web pages up to predetermined maximum pages and depth restrictions. Using TF-IDF representation and cosine similarity score, the Indexer creates an inverted index in pickle format. Top-ranked results are returned by the Processor based on the indexed material, which also handles free text queries in JSON format and carries out query validation and error-checking.

#### - Objectives:

   - Create a web crawler using Scrapy to download documents in HTML format.
  - Use TF-IDF representation to create an inverted index by implementing an indexer based on Scikit-Learn.
  - To rank documents during search indexing, apply cosine similarity score.
  - Build a Flask-based  processor that can process free-text queries and provide results that are ranked highly.
  - To improve the accuracy of query processing, make sure error-checking and query validation are in place.

#### - Next Steps:

  - Improve the web Crawler's scalability and efficiency by making it more efficient.
  - Improve the Indexer's performance by making it able to handle bigger datasets.
  - Use sophisticated search options like multidimensional search, wildcard search, and phrase search.
  - Provide an intuitive user interface to facilitate communication with the query processor.
  - Make sure the system is accurate and robust by conducting comprehensive testing and validation.

## Overview:

#### - Solution Outline:

  - Crawler: The web crawler uses Scrapy to retrieve web documents recursively up to specified maximum page and depth constraints after initializing with an initial URL . It guarantees effective and methodical web content retrieval while abiding by crawl policies and steering clear of duplicate content.

  - Indexer: Using TF-IDF representation and leveraging Scikit-Learn, the indexer creates an inverted index in pickle format. This makes it possible to store and retrieve document-term frequency data efficiently, facilitating quick and precise web content querying.

  - Processor: The JSON-formatted free text queries are handled by this Flask-implemented processor. In order to guarantee query integrity, it carries out error-checking and query validation. Then, using cosine similarity score, it returns results that are rated highest. Users who submit queries to the processor receive ranked, pertinent search results.

#### - Relevant Literature:

The proposed solution is inspired by the existing literature on web crawlers and search engine architectures. Scrapy has been widely used in the literature for web crawling because it provides a reliable and scalable framework for online scraping operations. Using Scikit-Learn to create an inverted index is a common practice in information retrieval and search engine design.

#### - Proposed System:

  - A reliable and effective method for accessing, indexing, and querying web content will be made available to users by the suggested system. 
  - The system strives to provide precise and pertinent search results while preserving scalability and performance by utilizing cutting-edge technologies and methodologies in web crawling, indexing, and query processing. 
  - Because of its modular design, the system is easily able to accommodate new features and improvements while being flexible enough to meet changing user expectations and requirements.


## Design:

#### - System Capabilities

1. Crawler: It is responsible for locating web information in HTML format.
   
-  Starts with a set of seed URLs or websites and tracks links up to a predetermined maximum depth or number of pages.
- Provides scalable and efficient web crawling by utilizing the Scrapy library.

2. Indexer:  Utilizing the downloaded web pages, this tool creates an inverted index.
  - Calculates the TF-IDF scores for each phrase found in the documents; the search results are ranked based on these values.
  - Returns the inverse index in a pickle format in terminal for easy retrieval.
  - The Scikit-Learn module is used to perform indexing and similarity calculations.

3. Processor: The Query Processor provides a user-friendly interface for organizing and handling search requests.
  - Confirms and processes user requests, ensuring proper input organization and error correction.
  - Cosine similarity calculations are used to extract the top-k ranked results of the inverted index.
  - Presents the search results in a clear and concise manner for the user.
  - Employed the Flask web framework to carry out the implementation.

#### - The following Interactions occur between these elements:

 - The web crawler starts with the seed URLs or websites and gathers web pages from the pre-approved goodreads websites.
 - After processing the downloaded web pages and generating the inverted index, the indexer component saves the TF-IDF-based representation of the content.
-  The query processor component receives a user-submitted search query, checks the data, pulls pertinent articles from the inverted index, and sorts the results based on cosine similarity.
 - The query processor then presents the top k search results to the user.

#### - Integration

  - These components work together to operate the search engine as a whole. The crawler supplies the content to be indexed, the indexer creates the data structures needed for efficient retrieval , and the query processor controls user input and results presentation. 
  - With popular frameworks and libraries such as Scikit-Learn, Flask, and Scrapy, the proposed system can be constructed in a modular and extensible manner, allowing for future updates and adjustments when needed.

## Architecture:

We are going to explain the software components, interfaces, and implementation specifics of the project in the architecture section:

#### - Components of software:

 Scrapy-based Web Crawler:

 - Scrapy Spider: Responsible for fetching HTML content, traversing links, and navigating web pages.
 - URL Manager: Oversees URL queue management, setting constraints on page count, depth, and starting URL/domain.
 - HTML Downloader: Retrieves HTML content of web pages.

 Scikit-Learn based Indexer module:
 - Document Processor: Extracts and preprocesses text from HTML content for indexing.
 - Indexer: Constructs an inverted index, computes TF-IDF scores, and saves the index as a pickle file.
 - Similarity Calculator: Computes cosine similarity between search queries and indexed documents.

Flask-based Processor Module:
 - Query Parser: Handles input validation, formatting, and error checking for user queries.
 - Retriever: Retrieves top search results from the inverted index based on cosine similarity.
 - Result Formatter: Presents search results in a user-friendly JSON format.

#### - Interfaces:

Interface between Crawler and Indexer: 
 - Facilitates the transfer of downloaded web documents from the crawler to the indexer.
 - Describes the methods and data formats used to transport document data.

Interface between the Indexer and Processor: 
 - Enables the indexer to send query results and indexed data to the processor.
 - Defines the format in which query parameters should be given in order to obtain ranked result

#### - Implementation Details:

Implementation of Crawler: 
 - Web crawling is done using the Scrapy framework.
 - Specified with max pages = 50, max depth= 2, and seed URL/domain = "https://www.goodreads.com/quotes".

Indexer Implementation: 
 - Utilizing Scikit-Learn, TF-IDF vectorization and cosine similarity computation  are implemented.
 - Printed the inverse index in pickle formatin the terminal itself for quick and easy access.
 - Also, Query vector shape, Cosine similarity shape is computed.

Processor Implementation: 
 - Using Flask to handle query queries, develops RESTful API endpoints.
 - Implements cosine similarity scores for ordering results and query validation/error-checking.
 - Parses and evaluates JSON-formatted requests before returning appropriate responses.
 - Finally, returns the cosine similarity score, author name, text and tags for the entered query.

## Operation:

I have used the Visual Studio Code application and run the following Commands.

#### - Software Commands:

Crawler:

 - "scrapy crawl goodreads_quotes": Initiates the web crawling process using the specified spider.

Indexer:
 - "python Indexer.py": Executes the indexer script to construct the inverted index.

Processor:
 - "python Processor.py": Runs the Flask-based processor for handling text queries.

#### - Inputs:

 Crawler:
 - Seed URL/Domain = "https://www.goodreads.com/quotes": The starting point for web crawling.
 - Max Pages = 50: The maximum number of web pages to crawl.
 - Max Depth = 2: The maximum depth of traversal for crawling.

 Indexer:
 - HTML content downloaded by the crawler = 'goodreads_quotes.html'.

 Processor:
 - JSON-formatted text queries for processing = "data.json".

#### - Installation:

Crawler Setup:
 - Install Scrapy: pip install scrapy
 - Create Scrapy project: scrapy startproject Crawler
 - Define spiders and settings as per project requirements.

Indexer Setup:
 - Install Scikit-Learn: pip install scikit-learn
 - Implement Indexer script to process HTML content and construct the inverted index.

Processor Setup:
 - Install Flask: pip install Flask
 - Develop Flask-based processor for query handling and result presentation.

Integration:
Ensure proper integration among the crawler, indexer, and processor components.

Execution:
Run the respective scripts or Flask application to execute the functionalities.

## Conclusion:


 Web crawler (Scrapy based):
   - Success: Using the seed URL or website that was supplied and adhering to the max pages and max depth limitations, the crawler successfully retrieves web content in HTML format.
   - Failure: The target domain may only be partially or completely crawled by the crawler as a result of problems like network faults, URL redirection, or unavailable web pages.
   - Outputs: The HTML content of the web pages that the crawler has downloaded is sent to the Indexer component.
   - Cautions/Warnings: The crawler should be built to elegantly handle edge scenarios, with retries for unsuccessful queries, respect for robots.txt, and no overloading of the target website.

  Indexer ( Scikit-Learn based):
   - Success: Using the received HTML material, the indexer successfully creates an inverted index, computes TF-IDF scores, and saves the index in a pickle file.
   - Failure: The indexer may run into problems with document processing, text extraction, or index generation, which could result in an erroneous or insufficient index.
   - Outputs: The Query Processor component uses the pickle file format that the indexer produces as its output, which is the inverted index.
   - Caveats/Cautions: The indexer should be built with memory utilization, disk space, and indexing efficiency in mind in order to properly manage large-scale indexing.

Flask-based Query Processor:
   - Success: The user requests are successfully processed by the query processor, which also verifies the input, pulls the first k results from the inverted index, and displays them in a JSON format.
   - Failure: The query processor can run into problems interpreting the query, retrieving results, or formatting the results, which would result in inaccurate or lacking responses.
   - Outputs: The query processor provides the user with a JSON format containing the top-k ranked search results.
   - Warnings and caveats: The query processor should be built with response time, error management, and scalability in mind in order to handle a large amount of user inquiries.

#### - Success Results:

 - The system efficiently crawls web documents and stores in html format in a seaparate file, indexes them using TF-IDF representation , and handles free-text queries, providing top ranked results.

#### - Outputs: 
 - Crawler: Downloaded web documents in HTML format.
 - Indexer: Printed Inverted inedx , Inverted index in pickle format, TF-IDF matrix shape, Query vector shape, cosine similarity shape and cosine similarity score.
 - Processor: JSON-formatted top-ranked search results based on user queries. In this Project it has printed authorname, text, tags based on the cosine similarity score for the entered query.

#### - Caveats/Cautions:

 - Web Crawling: Take care to observe terms of service and robots.txt directions, among other ethical and legal considerations, when crawling websites.
 - Indexing: To prevent noise and errors in indexing, make sure that text data has been properly preprocessed.
 - Query Processing: To efficiently handle a variety of user queries, put strong error handling and validation procedures in place.

## Data Sources:


#### Web Content:

 - The web crawling component of the project retrieves data from "Goodreads Quotes," a website hosted at https://www.goodreads.com/quotes.This website serves as a platform for sharing a wide range of quotes from various sources, authors, and genres. It offers a collection of web pages containing quotes, along with information about the authors and relevant tags. This data is utilized for indexing and search functionality within the project.

 - Flask Web Application: Data from the local web application, located at http://127.0.0.1:5000, powers the Flask-based query processing component. Through user interaction, the application allows users to submit free-text questions, from which the system gets pertinent data from the indexed web documents.


## Test cases:

  - Web Crawler: Content conformance to predetermined limits (seed URL/domain, max pages, max depth), successful crawling, and handling of edge cases (robots.txt, network failures, URL redirection).
   - Indexer: Accurate cosine similarity computations, accurate TF-IDF scores, and successful indexing of a variety of document formats.
   - Processor: JSON formatting, input validation, retrieval of the top-k results, and successful query handling.


## Source code:

### 1. crawl_spider.py:


 - Step 1: This code snippet begins by importing necessary modules, including Spider, Request, and CloseSpider from the Scrapy library. It defines a spider class called GoodreadsQuotesSpider, which inherits from Scrapy's Spider class.

 - Step 2: The spider is configured with attributes such as its name (goodreads_quotes), the allowed domains (goodreads.com), initial URLs to start crawling, and limitations such as max_pages = 50 and max_depth=2 to control the extent of crawling. Additionally, a counter (count) keeps track of the number of pages crawled.

- Step 3: The spider's purpose is to scrape quotes from Goodreads. It initializes an HTML string to store the extracted quotes and then parses the response, extracting quotes, authors, and tags. It also handles pagination to crawl through multiple pages of quotes. Finally, it saves the extracted data to an HTML file.

- Step 4: In the parse method, Scrapy processes each webpage response, extracting and parsing data. The extracted quotes are stored in an HTML string initialized at the beginning of the method.

- Step 5: If the page count exceeds one, the page counter is incremented. The method also checks if the allotted page count has been surpassed and raises a CloseSpider exception if necessary. Similarly, it verifies if the maximum depth has been reached and raises an exception if so.

- Step 6: Using CSS selectors, the method extracts quotes from the response. For each quote, it retrieves the content, author, and tags through looping. Finally, the extracted quotes are saved in an HTML file named "goodreads_quotes.html".

### 2. Indexer.py

#### Explanation:

- Step 1: The code imports necessary modules: Pickle, TfidfVectorizer, cosine_similarity, and BeautifulSoup.

- Step 2: It defines an Indexer class with methods:
  - _init_ : Constructs an inverted index, generates a TF-IDF matrix, retrieves documents, and initializes with filenames.
  - _retrieve_documents: Extracts quotes from HTML files by parsing them.
  - _build_inverted_index: Constructs an inverted index using the TF-IDF matrix.
  - search: Takes a query, calculates cosine similarity between documents, ranks them, and returns results.
  - print_index_as_pickle: Serializes and prints the inverted index in pickle format in terminal itself.
- Step 3: Example usage involves writing HTML content to a temporary file, initializing an Indexer with filenames, printing the inverted index, prompting for a query, performing a search, and displaying the results.
 - This code efficiently indexes and retrieves quotes from HTML documents, serving as a valuable tool for textual data analysis.


### 3. flask_processor.py


#### Explanation:

With the use of cosine similarity scores, this code configures a Flask web application for text data retrieval and query.

 - Step 1: The import section includes essential modules like render_template for HTML rendering, TfidfVectorizer for text vectorization, cosine_similarity for similarity scoring, request for HTTP request handling, and json for JSON data manipulation.

 - Step 2: In the Indexer class, the __init__ method begins with a list of documents. It calculates the TF-IDF matrix for each document and creates a TF-IDF vectorizer. The search method, when given a query, retrieves the k most similar documents based on cosine similarity scores.

 - Step 3: Data loading involves extracting information from a JSON file (data.json) and converting it into a list of documents.

 - Step 4: Creating an instance of the Indexer class initializes it with the document list, facilitating subsequent similarity searches.

 - Step 5: The Flask routes render the index.html template. The /query route handles POST requests containing a query in a JSON payload. After processing the query, the Indexer retrieves the top-k results, which are formatted and returned as a JSON response.

 - Step 6: The software is launched by starting Flask in debug mode to aid in debugging. Users can input queries, which are evaluated to find the most similar documents based on cosine similarity scores. JSON responses are then returned, including related data such as author names and tags.


## Bibliography:


#### 1.  I have referred the following youtube video for crawling using scrapy and did by taking the "goodreads.quotes" website  :

 - NeuralNine. "Crawling using Scrapy," YouTube video, NeuralNine, https://youtu.be/m_3gjHGxIJc?si=F4v2tKm7kzhbyBXN.

 - "Goodreads Quotes," Goodreads, https://www.goodreads.com/quotes.

#### 2. Also, I have taken the help from some AI tools such as chatgpt,copilot and perplexity for constructing an inverted index in pickel format.

 -  "ChatGPT," OpenAI, "https://chat.openai.com/c/0693a1dd-8f18-4541-b78e-a6cdbf408e3e".

 -  "Perplexity," OpenAI, "https://www.perplexity.ai/search/For-a-fixed-rBNiypq4TpaNJbjK0Lyjcg".

#### 3. I did my DBO project using flask. So, I have used the knowledge which i gained durig that project. Also, I learnt the flask from the following youtube link:

 - freecodecamp.org. "Flask tutorial," YouTube video, freecodecamp.org, https://youtu.be/Qr4QMBUPxWo?si=H-vWwj3BeSmJrt_a.

