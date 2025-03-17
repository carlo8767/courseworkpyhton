import heapq


def find_best_path(n, edges):
    # Initialize probabilities array
    # prob[i] represents best probability to reach lily i
    prob = [0] * (n + 1)
    prob[1] = 1.0  # Start with 100% probability at lily 1

    # Use negative probabilities for max-heap behavior (since heapq is a min-heap)
    pq = [(-1.0, 1)]  # (negative probability, node)

    while pq:
        curr_prob, curr_node = heapq.heappop(pq)
        curr_prob = -curr_prob  # Convert back to positive

        # If we've found a better path already, skip
        if curr_prob < prob[curr_node]:
            continue

        # Process all jumps from current lily
        for next_node, slip_prob in edges.get(curr_node, []):
            # Calculate probability of successful jump
            success_prob = 1.0 - slip_prob
            # Calculate new total probability to reach next_node
            new_prob = curr_prob * success_prob

            # If we found a better path, update and add to queue
            if new_prob > prob[next_node]:
                prob[next_node] = new_prob
                heapq.heappush(pq, (-new_prob, next_node))

    return prob[n]


def main():
    # Read input
    n, m = map(int, input().split())

    # Validate constraints
    if not (2 <= n <= 10000):
        print("Invalid number of lilies")
        return

    # Build graph as adjacency list with slip probabilities
    edges = {}
    for _ in range(m):
        i, j, p_ij = input().split()
        i, j = int(i), int(j)
        p_ij = float(p_ij)

        if i not in edges:
            edges[i] = []
        edges[i].append((j, p_ij))

    # Calculate and print result
    result = find_best_path(n, edges)
    print(f"{result:.6f}")


if __name__ == '__main__':
    main()