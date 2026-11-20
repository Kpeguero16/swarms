from contextlib import nullcontext
from types import SimpleNamespace

import pytest

from swarms.structs.ma_utils import reject_duplicate_names

WRITER = SimpleNamespace(agent_name="Writer")


@pytest.mark.parametrize(
    "agents, allow_same_object, raises",
    [
        ([WRITER, SimpleNamespace(agent_name="Writer")], True, True),
        ([WRITER, WRITER], True, False),
        ([WRITER, WRITER], False, True),
    ],
)
def test_reject_duplicate_names(agents, allow_same_object, raises):
    expected = (
        pytest.raises(ValueError, match="'Writer'. Swarm finds")
        if raises
        else nullcontext()
    )
    with expected:
        reject_duplicate_names(agents, "Swarm", allow_same_object)
