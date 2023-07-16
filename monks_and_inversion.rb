# only works with a small set of data
# https://www.hackerearth.com/practice/codemonk/?utm_source=new_user_signup&utm_medium=email&utm_campaign=codemonk

t = gets.chomp.to_i
(1..t).each do
    n = gets.chomp.to_i
    m = []
    (1..n).each do
        m.push gets.chomp.split(" ")
    end
    n -= 1
    counter = 0
    (0..n).each do |i|
        (0..n).each do |j|
            (i..n).each do |v|
                (j..n).each do |k|
                    counter += 1 if m[i][j].to_i > m[v][k].to_i
                end
            end
        end
    end
    pp counter
end
