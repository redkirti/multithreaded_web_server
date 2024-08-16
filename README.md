---

# Multithreaded Server Performance Analysis

## Overview

This project involves the implementation and performance analysis of a multithreaded server, which is benchmarked using a custom load generator. The server is tested on an 8-core system, with four cores dedicated to the server and the remaining four to the load generator. The goal of the project is to evaluate the server's throughput and response time under varying loads.

## System Requirements

- **Operating System**: Linux (with support for `taskset` command)
- **Compiler**: GCC with pthread library (`-lpthread`)
- **Python**: Python 3 with Matplotlib (`pyplot`) for plotting results

## Project Structure

- `server.c`: Multithreaded server source code.
- `load_gen.c`: Load generator source code.
- `script.sh`: Bash script for running the load generator and collecting data.
- `results.csv`: File where load generator results (throughput and response time) are stored.
- `plot.py`: Python script for plotting the throughput and response time against load.

## Compilation

### Server

To compile the server, run the following command:

```bash
make
```

### Load Generator

To compile the load generator, use the following command:

```bash
gcc -g -lpthread load_gen.c -o load_gen
```

## Running the Server

To run the server on the first four cores (cores 0-3) and listen on port 8080, use:

```bash
taskset -c 0-3 ./server 8080
```

## Load Generator Configuration and Execution

The load generator is configured to run on the last four cores (cores 4-7) for 10 iterations with varying user counts ranging from 200 to 2000. The think time between requests is set to 0.1 seconds, and the test duration is 60 seconds.

To run the load generator, use the following command template:

```bash
taskset -c 4-7 ./load_gen localhost 8080 <user_count> 0.1 60
```

Replace `<user_count>` with the desired number of users (e.g., 200, 400, ..., 2000).

## Data Collection

Data from the load generator is automatically appended to `results.csv` by running:

```bash
bash ./script.sh
```

The CSV file contains the following columns:
- **Load (User Count)**
- **Throughput**
- **Response Time**

### Sample Data

| Load | Throughput   | Response Time |
|------|--------------|---------------|
| 200  | 1972.31      | 0.001278      |
| 400  | 3949.53      | 0.001121      |
| 600  | 5902.01      | 0.001507      |
| 800  | 7666.57      | 0.004085      |
| 1000 | 7813.23      | 0.027640      |
| 1200 | 7860.80      | 0.052230      |
| 1400 | 7862.77      | 0.077485      |
| 1600 | 7845.84      | 0.103232      |
| 1800 | 7821.81      | 0.129217      |
| 2000 | 7791.52      | 0.155442      |

## Plotting Results

To visualize the server's performance, use the provided Python script to generate the plots:

```bash
python3 plot.py
```

### Graphs

1. **Throughput vs. Load**: 
   - The throughput increases linearly with the load until around 7500 requests/second, after which it stabilizes due to the server's processing limitations.

2. **Response Time vs. Load**:
   - The response time remains minimal and stable up to 600 users. Beyond this point, the response time increases exponentially as the server struggles to keep up with the incoming requests.

## Conclusion

This project demonstrates the performance characteristics of a multithreaded server under varying loads. The analysis shows that the server can handle up to a certain threshold efficiently, beyond which both throughput and response time are negatively impacted.

## Future Work

- **Optimization**: Explore server-side optimizations to improve performance beyond the current limits.
- **Scalability**: Investigate scaling strategies such as load balancing across multiple servers.
- **Advanced Metrics**: Include additional metrics such as CPU and memory utilization for a more comprehensive performance analysis.

---
