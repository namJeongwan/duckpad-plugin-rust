import CryptoKit
import Foundation
let args = CommandLine.arguments
guard args.count == 4 else { exit(64) }
var payload = Data("duckpad-extension-signature-v1\n".utf8)
payload.append(try Data(contentsOf: URL(fileURLWithPath: args[1])))
let signatureText = try String(contentsOfFile: args[2], encoding: .utf8).trimmingCharacters(in: .whitespacesAndNewlines)
guard let bytes = Data(base64Encoded: args[3]), let signature = Data(base64Encoded: signatureText) else { exit(65) }
let key = try Curve25519.Signing.PublicKey(rawRepresentation: bytes)
guard key.isValidSignature(signature, for: payload) else { exit(66) }
