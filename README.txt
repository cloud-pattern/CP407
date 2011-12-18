Robert Florance 
Scripts, Datasets, and Results for CP407

MAIN DIRECTORY:

    bookexamples/       - directory containing sample code
    results/            - directory containing csv result files
    datasets/           - directory containing txt datasets

    genNum.py           - generated original datasets (they get shuffled by each alg)
    genGraph.py         - generates randomized graphs and other graph tools    

    runAlg.sh           - used to run a group of datasets of a certain size range

    *.py                - the algorithms

INSTRUCTIONS FOR RUNNING ALGORITHMS:

    Sorting Algs:

    term$> python [algorithm filename] dataset/[filename] p

    Prim's and Dijkstra's Alg:

    term$> python [algorithm filename] [number of nodes] p

    N-Queens Alg:

    term$> python nqueens.py [board size] p

    N-Queens Monte Carlo Alg:

    term$> python nqueensMonteCarlo.py [board size] p

    NOTE: Don't forget the "p" on the end of each.  This tells the algorithm to print all results to the terminal, rather than write them to file.
 
