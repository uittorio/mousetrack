import QtQuick
import QtQuick.Controls.Basic
ApplicationWindow {
    id: applicationWindow
    property QtObject backend
    property string currTime: "00:00:00"
    visible: true
    width: 600
    height: 500
    title: "TrackMouse"

    Rectangle {
        id: mainContainer
        width: parent.width
        height: parent.height
        Image {
            source: "./images/mooncake.png"
            fillMode: Image.PreserveAspectFit
            width: 200
            anchors.right: mainContainer.right
        }
        Text {
            anchors {
                bottom: mainContainer.bottom
                bottomMargin: 12
                left: mainContainer.left
                leftMargin: 12
            }
            text: currTime
            font.pixelSize: 24
            color: "black"
        }
    }

    Connections {
        target: backend
        function onUpdated(msg) {
           currTime = msg;
        }
    }
}