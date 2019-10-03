# Copyright 2019 The Cirq Developers
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from typing import Iterator

from cirq.contrib.quirk.cells.cell import CellMaker
from cirq.contrib.quirk.cells.control_cells import (
    generate_all_control_cell_makers)
from cirq.contrib.quirk.cells.qubit_permutation_cells import (
    generate_all_qubit_permutation_cell_makers)
from cirq.contrib.quirk.cells.single_qubit_rotation_cells import (
    generate_all_single_qubit_rotation_cell_makers)


def generate_all_quirk_cell_makers() -> Iterator[CellMaker]:
    """Yields a `CellMaker` for every known Quirk gate, display, etc."""
    yield from generate_all_control_cell_makers()
    yield from generate_all_qubit_permutation_cell_makers()
    yield from generate_all_single_qubit_rotation_cell_makers()