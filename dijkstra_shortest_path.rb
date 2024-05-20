graph = {
  'A' => { 'B' => 1, 'C' => 4 },
  'B' => { 'A' => 1, 'C' => 2, 'D' => 5 },
  'C' => { 'A' => 4, 'B' => 2, 'D' => 1 },
  'D' => { 'B' => 5, 'C' => 1 }
}

def dijkstra (graph, start)
  distances = {}
  visited = {}

  nodes = graph.keys
  nodes.each { |node| distances[node] = Float::INFINITY }

  distances[start] = 0

  until nodes.empty?
    min_node = nodes.min_by { |node| visited[node] ? Float::INFINITY : distances[node] }
    break if distances[min_node] == Float::INFINITY

    graph[min_node].each do |neighbour, distance|
      alt = distances[min_node] + distance
      distances[neighbour] = alt if alt < distances[neighbour]
    end

    visited[min_node] = true
    nodes.delete(min_node)
  end

  distances
end

puts dijkstra(graph, 'A')
puts dijkstra(graph, 'B')
puts dijkstra(graph, 'C')
puts dijkstra(graph, 'D')
