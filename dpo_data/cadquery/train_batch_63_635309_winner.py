import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,61))
r=w0.sketch().segment((-93,-7),(-56,-20)).segment((-14,87)).segment((-53,100)).close().assemble().reset().face(w0.sketch().arc((52,41),(-38,-48),(93,-66)).arc((70,-27),(86,19)).arc((72,28),(57,32)).arc((54,38),(52,41)).assemble()).finalize().extrude(-122)