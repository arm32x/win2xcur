from typing import List

from wand.color import Color

from win2xcur.cursor import CursorFrame


def apply_to_frames(frames: List[CursorFrame], *, pad: float) -> None:
    for frame in frames:
        for cursor in frame:
            new_width = int(round(cursor.image.width * pad))
            new_height = int(round(cursor.image.height * pad))
            cursor.image.background_color = Color("transparent")
            cursor.image.extent(
                width=new_width,
                height=new_height,
                gravity="north_west", # this keeps the hotspot the same
            )
