import dxl_moduler

# シリアルポートを渡す
moduler = dxl_moduler.DxlClass("/dev/ttyUSB1")#COM1

# オペレーティングモードを指定（関数内で説明）
moduler.write_operating_mode(id=1, mode=3)
# トルクON
moduler.write_torque_state(id=1, state=1)
# ゴール指定
moduler.write_goal_position(id=1, goal_position=0)