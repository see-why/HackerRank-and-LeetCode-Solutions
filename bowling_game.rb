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

  def bowling_game_recursive(array)
    array, first, n = array_defaults(array)
    return first if n.zero?
    return bonus_for_strike(array, n) if strike?(array)
    return bonus_for_spare(array, n) if spare?(array)

    standard_bonus(array, n)
  end

  def bonus_for_strike(array, end_index)
    TEN + sum(array[1, 2]) + bowling_game_recursive(array[1, end_index])
  end

  def bonus_for_spare(array, end_index)
    TEN + array[2] + bowling_game_recursive(array[2, end_index])
  end

  def standard_bonus(array, end_index)
    sum(array[0, 2]) + bowling_game_recursive(array[2, end_index])
  end

  def strike?(array)
    array[0] == TEN && array.size > 3
  end

  def array_defaults(array)
    [array ||= [0], array.first, (array.size - 1)]
  end

  def spare?(array)
    array[0] ||= 0
    array[1] ||= 0
    array[0] + array[1] == TEN
  end

  def sum(array)
    array.inject(:+)
  end
end

# expect bowling_game([10] * 12) to be 300
# bolwing games rules: https://www.rookieroad.com/bowling/scoring-rules/
