# https://www.hackerrank.com/challenges/30-abstract-classes/problem?isFullScreen=true
class MyBook < Book
    attr_accessor :price
    attr_accessor :author, :title
    #   Class Constructor
    #   
    #   Parameters:
    #   title - The book's title.
    #   author - The book's author.
    #   price - The book's price.
    #
    # Write your constructor here
    
    def initialize(title, author, price)
        @title = title
        @author = author
        @price = price
    end
    
    
    #   Function Name: display
    #   Print the title, author, and price in the specified format.
    #
    # Write your function here
    def display()
        puts "Title: #{@title}"
        puts "Author: #{@author}"
        puts "Price: #{@price}"
    end

end
