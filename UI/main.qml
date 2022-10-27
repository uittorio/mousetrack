import QtQuick
import QtQuick.Controls.Basic
ApplicationWindow {
    id: applicationWindow
    property QtObject backend
    visible: true
    width: 600
    height: 500
    title: "TrackMouse"

    ListModel {
        id: eventList
    }

    Component {
        id: listComponent
        Row {
            spacing: 10
            Text {
                text: model.type;
                color: "black";
                font.pixelSize: 12
            }

            Text {
                text: model.time;
                color: "black";
                font.pixelSize: 12
            }
        }
    }

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
        ListView {
            anchors.fill: parent
            model: eventList
            delegate: listComponent
            clip: true
        }
    }

    Connections {
        target: backend
        function onUpdated(messages) {
            messages.forEach((message) => {
                eventList.append({"type": message.type, "time": message.time})
            })
        }
    }
}