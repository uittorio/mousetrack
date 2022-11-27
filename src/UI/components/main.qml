import QtQuick
import QtQuick.Controls
import QtCharts
import QtQuick.Layouts

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
    property QtObject percentageKeyboardEvents
    property real percentageKeyboardEventsValue
    visible: true
    width: 600
    height: 1000
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
            height: 300

            Grid {
                id: interactions
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

            Rectangle {
                anchors.top: interactions.bottom

                Column {
                    topPadding: 40
                    leftPadding: 40
                    spacing: 10;

                    Text {
                        id: keyboardPercentage
                        text: 'Keyboard % of total interactions'
                        anchors.leftMargin: 20
                        font.family: "Nunito"
                        font.weight: 300
                        font.pointSize: 16
                        color: "#1D1D1D"
                    }

                    Rectangle {
                        width: 310
                        height: 30

                        ProgressBar {
                            value: percentageKeyboardEventsValue
                        }
                    }
                }

            }
        }

        Rectangle {
            width: parent.width
            anchors.top: content.bottom
            height: 300

            ChartView {
                width: parent.width
                id: chartView
                height: 300

                LineSeries {
                    XYPoint {
                        x: 0
                        y: 0
                    }

                    XYPoint {
                        x: 10.1
                        y: 2.1
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

    Connections {
        target: percentageKeyboardEvents
        function onUpdated(percentage) {
            percentageKeyboardEventsValue = percentage;
        }
    }
}