import QtQuick
import QtQuick.Controls.Basic

ApplicationWindow {
    id: applicationWindow
    property QtObject clickEventsUpdater
    property int clickEventsCount
    property QtObject scrollEventsUpdater
    property int scrollEventsCount
    property QtObject moveEventsUpdater
    property int moveEventsCount
    property QtObject keyboardEventsUpdater
    property int keyboardEventsCount
    visible: true
    width: 600
    height: 500
    title: "Mouse Track"

    Rectangle {
        id: mainContainer
        width: parent.width
        height: parent.height

        Header {
            id: headerContainer
        }

        Rectangle {
            id: content
            anchors.top: headerContainer.bottom
            width: parent.width
            height: parent.height

            Grid {
                spacing: 60
                columns: 2
                Column {
                    id: leftContentColumn
                    topPadding: 40
                    leftPadding: 40
                    width: 100;
                    spacing: 10;

                    Interaction {
                        text: "Click"
                        image: "./images/click.png"
                        countText: clickEventsCount
                    }

                    Interaction {
                        text: "Scroll"
                        image: "./images/scroll.png"
                        countText: scrollEventsCount
                    }

                    Interaction {
                        text: "Move"
                        image: "./images/move.png"
                        countText: moveEventsCount
                    }
                }

                Column {
                    id: rightColumnContent
                    topPadding: 40
                    leftPadding: 40
                    width: 100;
                    spacing: 10;

                    Interaction {
                        text: "Key press"
                        image: "./images/keyboard.png"
                        countText: keyboardEventsCount
                    }
                }
            }


        }
    }

    Connections {
        target: clickEventsUpdater
        function onUpdated(messages) {
            clickEventsCount = messages.length;
        }
    }

    Connections {
        target: scrollEventsUpdater
        function onUpdated(messages) {
            scrollEventsCount = messages.length;
        }
    }

    Connections {
        target: moveEventsUpdater
        function onUpdated(messages) {
            moveEventsCount = messages.length;
        }
    }

    Connections {
        target: keyboardEventsUpdater
        function onUpdated(messages) {
            keyboardEventsCount = messages.length;
        }
    }
}