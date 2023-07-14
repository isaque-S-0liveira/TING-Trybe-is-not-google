import pytest
from ting_file_management.priority_queue import PriorityQueue


def test_basic_priority_queueing():
    mock_file = [
        {
            "nome_do_arquivo": "f1.txt",
            "qtd_linhas": 4,
            "linhas": [1, 2, 3, 4],
        },
        {
            "nome_do_arquivo": "f2.txt",
            "qtd_linhas": 9,
            "linhas": [1, 2, 3, 4, 5, 6, 7, 8, 9],
        },
        {
            "nome_do_arquivo": "f3.txt",
            "qtd_linhas": 1,
            "linhas": [1],
        },
        {
            "nome_do_arquivo": "f4.txt",
            "qtd_linhas": 1,
            "linhas": [1],
        },
    ]
    queue = PriorityQueue()
    for f in mock_file:
        queue.enqueue(f)

    assert len(queue) == len(mock_file)
    assert queue.search(0) == mock_file[0]
    queue.dequeue()
    assert queue.search(0) == mock_file[2]
    with pytest.raises(IndexError):
        queue.search(-1)
