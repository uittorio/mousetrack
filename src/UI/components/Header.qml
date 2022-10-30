import QtQuick

Rectangle {
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