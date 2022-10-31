# playground class
class Playground
  TEN = 10

  def initialize(number_of_children = nil, rolls = nil)
    @children = number_of_children
    @rolls = rolls
  end

  def empty?
    @children.zero?
  end

  def mood
    'boring'
  end

  def bowling_game(array, n = array.size - 1, first = array[0])
    return first if n.zero?
    return first + sum(array[1, 2]) + bowling_game(array[1, n]) if strike?(array)

    return sum(array[0, 3]) + bowling_game(array[2, n]) if spare?(array)

    first + bowling_game(array[1, n])
  end

  def strike?(array)
    array[0] == TEN && array.size > 3
  end

  def spare?(array)
    array[0] + array[1] == TEN
  end

  def sum(array)
    array.inject(:+)
  end

end

# expect bowling_game([10] * 12) to be 300
