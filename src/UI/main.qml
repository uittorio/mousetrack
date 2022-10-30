import QtQuick
import QtQuick.Controls.Basic
import "./components"

ApplicationWindow {
    id: applicationWindow
    property QtObject clickEvents
    property int clickEventCount
    visible: true
    width: 600
    height: 500
    title: "Mouse Track"

    Rectangle {
        id: mainContainer
        width: parent.width
        height: parent.height

        Rectangle {
            id: headerContainer
            width: parent.width
            height: 60
            color: "#6EC781"
            Row {
                leftPadding: 40
                anchors.verticalCenter: parent.verticalCenter;
                Text {
                    text: "Mouse Track"
                    font.family: "Nunito"
                    font.weight: 300
                    font.pointSize: 24
                    color: "#1D1D1D"
                }
            }
        }

        Rectangle {
            id: content
            anchors.top: headerContainer.bottom
            width: parent.width
            height: parent.height

            Column {
                id: leftContentColumn
                topPadding: 40
                leftPadding: 40
                width: 100;
                spacing: 10;

                Interaction {
                    text: "Click"
                    image: "./images/click.png"
                    countText: clickEventCount
                }

                Interaction {
                    text: "Scroll"
                    image: "./images/scroll.png"
                    countText: clickEventCount
                }

                Interaction {
                    text: "Move"
                    image: "./images/move.png"
                    countText: clickEventCount
                }
           }
        }
    }

    Connections {
        target: clickEvents
        function onUpdated(messages) {
            clickEventCount = messages.length;
        }
    }
}