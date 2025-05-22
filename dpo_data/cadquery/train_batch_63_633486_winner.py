import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-40))
r=w0.sketch().segment((-82,-64),(-68,-64)).segment((-68,-84)).segment((-7,-84)).segment((-7,-92)).segment((24,-92)).segment((24,-84)).segment((86,-84)).segment((86,-64)).segment((100,-64)).segment((100,15)).segment((86,15)).segment((86,35)).segment((50,35)).arc((-57,84),(-82,-33)).close().assemble().finalize().extrude(80)