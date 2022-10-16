=begin
# [1,2] => power[0,0] = min(1) * sum(1) = 1 * 1 = 1
power[0,1] = min(1,2) * sum(1,2) = 1 * 3 = 3
power[1,1] = min(2) * sum(2) = 2 * 2 = 4

sum of powers = 1 + 3 + 4 = 8
=end

def full_power(power)
    sum = 0
    for i in 0...power.length
        sum += recursive_power(power, i, power.length-1)
    end
    sum
end

def recursive_power(sub_power, i, j)
    if i == j
        return unit_power(sub_power[i..j])
    else
        return unit_power(sub_power[i..j]) + recursive_power(sub_power, i, j-1)
    end
end

def unit_power(sub_power)
    sub_power.min * sub_power.inject(&:+)
end

puts full_power [1,2,3,4,5] # 238
puts full_power [1,1,1,1,1] # 35
