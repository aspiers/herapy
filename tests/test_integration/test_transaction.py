import aergo.herapy as herapy


def test_tx(aergo) -> None:
    print("------ Set Sender Account -----------")
    sender_private_key = \
        "eHoEcHnaxpGpgzknXjuwon8VFVrLkKHC4FckGuGkQ8depiDDfyUAWC3L"
    sender_account = aergo.new_account(private_key=sender_private_key)
    print("  > Sender Address: {}".format(sender_account.address))
    aergo.get_account()
    print("    > account state of Sender")
    print("      - balance        = {}".format(sender_account.balance))
    print("      - nonce          = {}".format(sender_account.nonce))
    print("      - code hash      = {}".format(sender_account.code_hash))
    print("      - storage root   = {}".format(sender_account.storage_root))

    print("------ Set Receiver Account -----------")
    receiver_address = "AmMPQqRJ4pd8bS9xdkw5pjExtLjaUXaYGB5kagzHu4A9ckKgnBV2"
    print("  > Receiver Address: {}".format(receiver_address))
    receiver_account = aergo.get_account(address=receiver_address)
    print("    > account state of Sender")
    print("      - balance        = {}".format(receiver_account.balance))
    print("      - nonce          = {}".format(receiver_account.nonce))
    print("      - code hash      = {}".format(receiver_account.code_hash))
    print("      - storage root   = {}".format(receiver_account.storage_root))

    print("------ Simple Send Tx -----------")
    simple_tx, result = aergo.send_payload(to_address=receiver_address,
                                           amount=10, payload=None,
                                           retry_nonce=3)
    print("  > simple TX[{}]".format(simple_tx.calculate_hash()))
    print("{}".format(str(simple_tx)))
    print("  > result: ", result)
    assert result.status == herapy.CommitStatus.TX_OK, \
        "    > ERROR[{0}]: {1}".format(result.status, result.detail)
    print("    > result[{0}] : {1}".format(result.tx_id, result.status.name))

    aergo.wait_tx_result(simple_tx.tx_hash)

    print("------ Check TX in Aergo -----------", flush=True)
    tx = aergo.get_tx(simple_tx.tx_hash)
    print(" TX from Aergo: ", str(tx))
    tx = tx.block.get_tx(tx.index_in_block)
    print(" TX in Block: ", str(tx))

    print("------ Check TX status -----------")
    print("  > TX: {}".format(str(simple_tx.tx_hash)))
    tx_result = aergo.get_tx_result(simple_tx.tx_hash)
    print("      result: ", tx_result)
    assert tx_result.status == herapy.TxResultStatus.SUCCESS, \
        "  > ERROR[{0}]:{1}: {2}".format(
            tx_result.contract_address, tx_result.status, tx_result.detail)

    print("------ Get Sender Account Info -----------")
    aergo.get_account()
    print("    > account state of Sender")
    print("      - balance        = {}".format(sender_account.balance))
    print("      - nonce          = {}".format(sender_account.nonce))
    print("      - code hash      = {}".format(sender_account.code_hash))
    print("      - storage root   = {}".format(sender_account.storage_root))

    print("------ Create Tx -----------")
    tx = herapy.Transaction(from_address=bytes(sender_account.address),
                            nonce=sender_account.nonce + 1,
                            amount=10)
    tx.to_address = herapy.utils.decode_address(receiver_address)
    tx.chain_id = aergo.chain_id
    print("  > unsigned TX Hash: {}".format(tx.tx_hash))
    print("  > unsigned TX : {}"
          .format(herapy.utils.convert_tx_to_formatted_json(tx)))

    print("------ Sign Tx -----------")
    tx.sign = sender_account.sign_msg_hash(
        tx.calculate_hash(including_sign=False))
    print("  > TX Signature: {}".format(tx.sign_str))
    print("  > TX Hash: {}".format(tx.tx_hash))
    print("  > TX : {}".format(herapy.utils.convert_tx_to_formatted_json(tx)))

    print("------ Send Tx -----------")
    tx, result = aergo.send_tx(tx)
    print("{}".format(herapy.utils.convert_tx_to_formatted_json(tx)))
    assert result.status == herapy.CommitStatus.TX_OK, \
        "    > ERROR[{0}]: {1}".format(result.status, result.detail)
    print("    > result[{0}] : {1}".format(result.tx_id, result.status.name))

    aergo.wait_tx_result(tx.tx_hash)

    aergo.get_account()
    print("    > account state of Sender")
    print("      - balance        = {}".format(sender_account.balance))
    print("      - nonce          = {}".format(sender_account.nonce))
    print("      - code hash      = {}".format(sender_account.code_hash))
    print("      - storage root   = {}".format(sender_account.storage_root))
