import QtQuick

Rectangle {
    id: container
    property alias text: label.text
    property string image: ""
    height: 50
    width: 200

    Image {
        id: image
        source: container.image;
        fillMode: Image.PreserveAspectFit
        height: parent.height
    }

    Text {
        id: label
        anchors.left: image.right
        anchors.verticalCenter: image.verticalCenter;
        text: text
        font.family: "Nunito"
        font.weight: 200
        font.pointSize: 12
        color: "#1D1D1D"
    }
}