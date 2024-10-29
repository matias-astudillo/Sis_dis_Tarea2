import grpc
from flask import Flask, request, jsonify
from order_management_pb2 import Order, OrderStatusRequest
from order_management_pb2_grpc import OrderManagementStub

app = Flask(__name__)

def create_grpc_stub():
    channel = grpc.insecure_channel('order_management:50051')
    return OrderManagementStub(channel)

# Para poder enviar pedidos al servidor grpc para que puedan ser procesados
@app.route('/send_order', methods=['POST'])
def send_order():
    order_data = request.json
    order = Order(
        product_name=order_data['product_name'],
        price=order_data['price'],
        payment_gateway=order_data['payment_gateway'],
        card_brand=order_data['card_brand'],
        bank=order_data['bank'],
        shipping_direction=order_data['shipping_direction'],
        email=order_data['email']
    )
    stub = create_grpc_stub()
    response = stub.CreateOrder(order)
    return jsonify({"id": response.order_id})

# Para consultar el estado de un pedido al servidor grpc
@app.route('/check_order_status', methods=['GET'])
def check_order_status():
    order_id_request = str(request.args.get('order_id'))
    stub = create_grpc_stub()
    orderStatusRequest = OrderStatusRequest(
        order_id = order_id_request
    )
    status_response = stub.GetOrderStatus(orderStatusRequest)
    return jsonify({"order_id": order_id_request, "status": status_response.status})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5008)