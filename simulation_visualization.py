import time
import pybullet_data
import pybullet as p
from pybullet import URDF_USE_SELF_COLLISION, URDF_MAINTAIN_LINK_ORDER, URDF_USE_SELF_COLLISION_INCLUDE_PARENT


def simulation_visualization(urdf, height):
    # Connect to Physics-Server
    p.connect(p.GUI)
    # Disable sidebars
    p.configureDebugVisualizer(p.COV_ENABLE_GUI, 0)
    # Set camera position
    p.resetDebugVisualizerCamera(
        cameraDistance=1.5, cameraYaw=90, cameraPitch=-20, cameraTargetPosition=[0, 0, 1.0])
    if p.getConnectionInfo():
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        humanoid_0 = p.loadURDF('./workers/' + urdf, [0.0, 0.0, height], p.getQuaternionFromEuler([0.0, 0.0, 0.0]), globalScaling=1,
                                useFixedBase=1, flags=URDF_MAINTAIN_LINK_ORDER | URDF_USE_SELF_COLLISION_INCLUDE_PARENT | URDF_USE_SELF_COLLISION)
        # Load plane
        p.loadURDF('./plane/plane100.urdf', [0, 0, -0.001])
        p.setGravity(0, 0, -9.806)
        p.setRealTimeSimulation(1)
        # Arms ids (this is the hand of the humanoid)
        l_arm = 39
        r_arm = 40
        # Avoid termination
        while p.isConnected():
            try:
                display_hand_positions_vis(
                    humanoid_0, height, l_arm, r_arm, 0.0, 1, 2)
            except:
                pass
            time.sleep(1. / 240.)


def display_hand_positions_vis(humanoid, height, l_arm, r_arm, threshold, id1, id2):
    ls_l = p.getLinkState(humanoid, l_arm)
    ls_r = p.getLinkState(humanoid, r_arm)
    info_header = 'Right / Left end-effector position (x, y, z)'
    info_text_l = str(format((ls_l[4][0]), '.3f')) + ', ' + str(format(
        (ls_l[4][1] - threshold), '.3f')) + ', ' + str(format((ls_l[4][2]), '.3f'))
    info_text_r = str(format((ls_r[4][0]), '.3f')) + ', ' + str(format(
        (ls_r[4][1] - threshold), '.3f')) + ', ' + str(format((ls_r[4][2]), '.3f'))
    # Add info text
    p.addUserDebugText(text=info_header, textPosition=[
                       0.0, 0.0 + threshold, height + 0.5], textColorRGB=[0.2, 0.2, 0.2], replaceItemUniqueId=id1)
    p.addUserDebugText(text=info_text_r + ' / ' + info_text_l, textPosition=[
                       0.0, 0.0 + threshold, height + 0.4], textColorRGB=[0.2, 0.2, 0.2], replaceItemUniqueId=id2)
